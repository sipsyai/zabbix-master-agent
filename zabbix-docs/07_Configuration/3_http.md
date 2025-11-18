---
title: HTTP template operation
source: https://www.zabbix.com/documentation/current/en/manual/config/templates_out_of_the_box/http
downloaded: 2025-11-14 10:36:04
---

# 3 HTTP template operation

Steps to ensure correct operation of templates that collect metrics with the [HTTP agent](/documentation/current/en/manual/config/items/itemtypes/http):

1\. Create a host in Zabbix and specify an IP address or DNS name of the monitoring target as the main interface. This is needed for the {HOST.CONN} macro to resolve properly in the template items.  
2\. [Link](/documentation/current/en/manual/config/templates/linking#linking-a-template) the template to the host created in step 1 (if the template is not available in your Zabbix installation, you may need to [import](/documentation/current/en/manual/config/templates_out_of_the_box#template-upgrade) the template first).  
3\. If necessary, adjust the values of template macros.  
4\. Configure the instance being monitored to allow data sharing with Zabbix.

A detailed description of a template, including the full list of macros, items and triggers, is available in the template's README file (accessible by clicking on a template name).

The following templates are available:

  * [Acronis Cyber Protect Cloud by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/acronis/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Apache by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/apache_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Asterisk by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/tel/asterisk_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [AWS by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/cloud/AWS/aws_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [AWS Cost Explorer by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/cloud/AWS/aws_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [AWS EC2 by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/cloud/AWS/aws_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [AWS ECS Cluster by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/cloud/AWS/aws_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [AWS ECS Serverless Cluster by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/cloud/AWS/aws_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [AWS ELB Application Load Balancer by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/cloud/AWS/aws_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [AWS ELB Network Load Balancer by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/cloud/AWS/aws_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [AWS Lambda by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/cloud/AWS/aws_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [AWS RDS instance by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/cloud/AWS/aws_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [AWS S3 bucket by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/cloud/AWS/aws_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Azure by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/cloud/azure_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Cisco Meraki organization by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/net/meraki_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Cisco SD-WAN by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/net/cisco/cisco_sdwan_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Cisco Secure Firewall Threat Defense by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/net/cisco/cisco_secure_ftd_http/README.md?at=release%2F7.4)
  * [ClickHouse by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/clickhouse_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Cloudflare by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/cloudflare_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [CockroachDB by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/cockroachdb_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Control-M enterprise manager by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/controlm_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Control-M server by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/controlm_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [DELL PowerEdge R720 by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/server/dell/dell_r720_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [DELL PowerEdge R740 by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/server/dell/dell_r740_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [DELL PowerEdge R820 by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/server/dell/dell_r820_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [DELL PowerEdge R840 by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/server/dell/dell_r840_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Elasticsearch Cluster by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/elasticsearch_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Envoy Proxy by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/envoy_proxy_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Etcd by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/etcd_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [FortiGate by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/net/fortinet/fortigate_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [GitHub repository by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/github_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [GitLab by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/gitlab_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Google Cloud Platform (GCP) by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/cloud/gcp/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Hadoop by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/hadoop_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [HAProxy by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/haproxy_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [HashiCorp Consul Cluster by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/consul_http/consul_cluster/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [HashiCorp Consul Node by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/consul_http/consul/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [HashiCorp Nomad by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/nomad/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [HashiCorp Vault by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/vault_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Hikvision camera by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/cctv/hikvision/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [HPE iLO by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/server/hpe_ilo_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [HPE MSA 2040 Storage by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/san/hpe_msa2040_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [HPE MSA 2060 Storage by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/san/hpe_msa2060_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [HPE Primera by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/san/hpe_primera_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [HPE Synergy by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/server/hpe_synergy_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [InfluxDB by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/influxdb_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Jenkins by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/jenkins/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Kubernetes API server by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/kubernetes_http/kubernetes_api_server_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Kubernetes cluster state by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/kubernetes_http/kubernetes_state_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)  

  * [Kubernetes Controller manager by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/kubernetes_http/kubernetes_controller_manager_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)  

  * [Kubernetes kubelet by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/kubernetes_http/kubernetes_kubelet_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)  

  * [Kubernetes nodes by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/kubernetes_http/kubernetes_nodes_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Kubernetes Scheduler by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/kubernetes_http/kubernetes_scheduler_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [MantisBT by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/mantisbt/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Microsoft 365 reports by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/ms365_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Microsoft SharePoint by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/sharepoint_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [NetApp AFF A700 by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/san/netapp_aff_a700_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Nextcloud by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/nextcloud/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [NGINX by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/nginx_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [NGINX Plus by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/nginx_plus_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Nutanix Prism Element by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/nutanix_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [OpenStack by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/cloud/openstack/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [OpenWeatherMap by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/openweathermap_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Oracle Cloud by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/cloud/oracle_cloud/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Palo Alto PA-440 by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/net/paloalto/paloalto_pa440/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [PHP-FPM by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/php-fpm_agent/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Proxmox VE by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/proxmox/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Pure Storage FlashArray v1 and v2 by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/san/pure_storage_flasharray/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [RabbitMQ cluster by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/rabbitmq_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [TiDB by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/tidb_http/tidb_tidb_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [TiDB PD by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/tidb_http/tidb_pd_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [TiDB TiKV by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/tidb_http/tidb_tikv_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Travis CI by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/travis_ci_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Veeam Backup Enterprise Manager by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/veeam/enterprise_manager_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [Veeam Backup and Replication by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/veeam/backup_replication_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [VMware SD-WAN VeloCloud by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/net/velocloud_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [YugabyteDB by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/db/yugabytedb_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)
  * [ZooKeeper by HTTP](https://git.zabbix.com/projects/ZBX/repos/zabbix/browse/templates/app/zookeeper_http/README.md?at=refs%2Fheads%2Frelease%2F7.4)