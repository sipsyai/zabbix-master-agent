---
title: Preprocessing details
source: https://www.zabbix.com/documentation/current/en/manual/config/items/preprocessing/preprocessing_details
downloaded: 2025-11-14 10:34:46
---

# 2 Preprocessing details

#### Overview

This section provides item value preprocessing details. The item value preprocessing allows to define and execute [transformation rules](/documentation/current/en/manual/config/items/preprocessing) for the received item values.

Preprocessing is managed by the preprocessing manager process along with preprocessing workers that perform the preprocessing steps. All values with preprocessing (before Zabbix 7.4.1, all values), received from different data gatherers, pass through the preprocessing manager before being added to the history cache. Socket-based IPC communication is used between data gatherers (pollers, trappers, etc.) and the preprocessing process. Either Zabbix server or Zabbix proxy (for the items monitored by the proxy) performs the preprocessing steps.

#### Item value processing

To visualize the data flow from data source to the Zabbix database, we can use the following simplified diagram:

![](/documentation/current/assets/en/manual/appendix/items/overall_pic.png)

The diagram above shows only processes, objects and actions related to item value processing in a **simplified** form. The diagram does not show conditional direction changes, error handling or loops. The local data cache of the preprocessing manager is not shown either because it doesn't affect the data flow directly. The aim of this diagram is to show processes involved in the item value processing and the way they interact.

  * Data gathering starts with raw data from a data source. At this point, the data contains only ID, timestamp and value (can be multiple values as well).
  * No matter what type of data gatherer is used, the idea is the same for active or passive checks, for trapper items, etc., as it only changes the data format and the communication starter (either data gatherer is waiting for a connection and data, or data gatherer initiates the communication and requests the data). The raw data is validated, the item configuration is retrieved from the configuration cache (data is enriched with the configuration data).
  * A socket-based IPC mechanism is used to pass data from data gatherers to the preprocessing manager. At this point the data gatherer continues to gather data without waiting for the response from preprocessing manager.
  * Data preprocessing is performed. This includes the execution of preprocessing steps and dependent item processing.

An item can change its state to NOT SUPPORTED while preprocessing is performed if any of preprocessing steps fail.

  * The history data from the local data cache of the preprocessing manager is being flushed into the history cache.
  * At this point the data flow stops until the next synchronization of history cache (when the history syncer process performs data synchronization).
  * The synchronization process starts with data normalization before storing data in Zabbix database. The data normalization performs conversions to the desired item type (type defined in item configuration), including truncation of textual data based on predefined sizes allowed for those types (HISTORY_STR_VALUE_LEN for string, HISTORY_TEXT_VALUE_LEN for text and HISTORY_LOG_VALUE_LEN for log values). The data is being sent to the Zabbix database after the normalization is done.

An item can change its state to NOT SUPPORTED if data normalization fails (for example, when a textual value cannot be converted to number).

  * The gathered data is being processed - triggers are checked, the item configuration is updated if item becomes NOT SUPPORTED, etc.
  * This is considered the end of data flow from the point of view of item value processing.

#### Item value preprocessing

Data preprocessing is performed in the following steps:

  * If the item has neither preprocessing nor dependent items, its value is either added to the history cache or sent to the LLD manager. Otherwise, the item value is passed to the preprocessing manager using a UNIX socket-based IPC mechanism (before Zabbix 7.4.1, all values are passed through the preprocessing manager before being added to the history cache or sent to the LLD manager).
  * A preprocessing task is created and added to the queue and preprocessing workers are notified about the new task.
  * At this point the data flow stops until there is at least one unoccupied (i.e., not executing any tasks) preprocessing worker.
  * When a preprocessing worker is available, it takes the next task from the queue.
  * After the preprocessing is done (both failed and successful execution of preprocessing steps), the preprocessed value is added to the finished task queue and the manager is notified about a new finished task.
  * The preprocessing manager converts the result to desired format (defined by item value type) and either adds it to the history cache or sends to the LLD manager.
  * If there are dependent items for the processed item, then dependent items are added to the preprocessing queue with the preprocessed master item value. Dependent items are enqueued bypassing the normal value preprocessing requests, but only for master items with the value set and not in a NOT SUPPORTED state.

![](/documentation/current/assets/en/diagrams/value_preprocessing.png)

Note that in the diagram the master item preprocessing is slightly simplified by skipping the preprocessing caching.

#### Preprocessing queue

The preprocessing queue is organized as:

  * the list of pending tasks: 
    * tasks created directly from value preprocessing requests in the order they were received
  * the list of immediate tasks (processed before pending tasks): 
    * testing tasks (created in response to item/preprocessing testing requests by the frontend)
    * dependent item tasks
    * sequence tasks (tasks that must be executed in a strict order): 
      * having preprocessing steps using the last value: 
        * change
        * throttling
        * JavaScript (bytecode caching)
      * dependent item preprocessing caching
  * the list of finished tasks

#### Preprocessing caching

Preprocessing caching was introduced to improve the preprocessing performance for multiple dependent items having similar preprocessing steps (which is a common LLD outcome).

Caching is done by preprocessing one dependent item and reusing some of the internal preprocessing data for the rest of the dependent items. The preprocessing cache is supported only for the first preprocessing step of the following types:

  * Prometheus pattern (indexes input by metrics)
  * JSONPath (parses the data into object tree and indexes the first expression `[?(@.path == "value")]`)

#### Preprocessing workers

The Zabbix server configuration file allows users to set the count of preprocessing worker threads. The [StartPreprocessors](/documentation/current/en/manual/appendix/config/zabbix_server#startpreprocessors) configuration parameter should be used to set the number of pre-started instances of preprocessing workers, which should at least match the number of available CPU cores.

If preprocessing tasks are not CPU-bound and involve frequent network requests, configuring additional workers is recommended. The optimal number of preprocessing workers can be determined by many factors, including the count of "preprocessable" items (items that require to execute any preprocessing steps), the count of data gathering processes, the average step count for item preprocessing, etc. Insufficient workers can lead to high memory usage. For troubleshooting excessive memory usage on your Zabbix installation, see [Profiling excessive memory usage with tcmalloc](/documentation/current/en/manual/installation/known_issues#profiling-excessive-memory-usage-with-tcmalloc).

But assuming that there are no heavy preprocessing operations like parsing large XML/JSON chunks, the number of preprocessing workers can match the total number of data gatherers. This way, there will mostly (except for the cases when data from the gatherer comes in bulk) be at least one unoccupied preprocessing worker for collected data.

Too many data gathering processes (pollers, unreachable pollers, ODBC pollers, HTTP pollers, Java pollers, pingers, trappers, proxypollers) together with IPMI manager, SNMP trapper and preprocessing workers can exhaust the per-process file descriptor limit for the preprocessing manager.   
  
Exhausting the per-process file descriptor limit will cause Zabbix server to stop, typically shortly after startup but sometimes taking longer. To avoid such issues, review the [Zabbix server configuration file](/documentation/current/en/manual/appendix/config/zabbix_server) to optimize the number of concurrent checks and processes. Additionally, if necessary, ensure that the file descriptor limit is set sufficiently high by checking and adjusting system limits.

##### Value processing pipeline

Item value processing is executed in multiple steps (or phases) by multiple processes. This can cause:

  * A dependent item can receive values, while THE master value cannot. This can be achieved by using the following use case: 
    * Master item has value type `UINT` (trapper item can be used), dependent item has value type `TEXT`.
    * No preprocessing steps are required for both master and dependent items.
    * Textual value (for example, "abc") should be passed to master item.
    * As there are no preprocessing steps to execute, preprocessing manager checks if master item is not in NOT SUPPORTED state and if value is set (both are true) and enqueues dependent item with the same value as master item (as there are no preprocessing steps).
    * When both master and dependent items reach history synchronization phase, master item becomes NOT SUPPORTED because of the value conversion error (textual data cannot be converted to unsigned integer).

As a result, the dependent item receives a value, while the master item changes its state to NOT SUPPORTED.

  * A dependent item receives value that is not present in the master item history. The use case is very similar to the previous one, except for the master item type. For example, if `CHAR` type is used for master item, then master item value will be truncated at the history synchronization phase, while dependent items will receive their values from the initial (not truncated) value of the master item.