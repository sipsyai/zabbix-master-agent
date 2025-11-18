---
title: Upgrade notes for 7.4.x
source: https://www.zabbix.com/documentation/current/en/manual/installation/upgrade_notes_minor
downloaded: 2025-11-14 10:34:24
---

# 11 Upgrade notes for 7.4.x

This page provides collective upgrade notes for minor releases of the major Zabbix version.

See also [upgrade notes](/documentation/current/en/manual/installation/upgrade_notes) of the major version.

## Upgrade notes for 7.4.4

**Warning!** Upgrading to this version is not recommended due to [errors](/documentation/current/en/manual/installation/known_issues#known-issues-in-7.4.4) related to graphs and the Zabbix agent 2 MySQL plugin.

## Upgrade notes for 7.4.3

#### PHP cURL minimum version

The minimum supported version for the cURL [PHP extension](/documentation/current/en/manual/installation/requirements#frontend) is now 7.19.4.

## Upgrade notes for 7.4.1

#### Agent 2 runtime control output stream

Zabbix agent 2 [runtime control](/documentation/current/en/manual/concepts/agent2#runtime-control) commands (`zabbix_agent2 -R <option>`) now write output to `stdout` (standard output) instead of `stderr` (standard error). Please update any scripts that rely on previous behavior.