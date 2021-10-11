[back to api overview](../api_overview.md#api)

## /v1/vsphere/vm/inspect
虚拟机详情
### 请求类型
GET

### 请求参数

 名称 | 参数类型 | 是否必填 | 默认值 | 描述
--- |---|---|--- |---
 vsphere_uuid|string| 是|-  | vsphere uuid
 vm_reference|string|是|-|虚拟机的唯一标识

### 返回参数

名称|参数类型|描述
---|---|---
TODO

### 示例

#### 请求示例
```
http://192.168.201.25:9990/v1/vsphere/vm/inspect?vsphere_uuid=757a9afa-5a01-11e9-b9ab-5256fffab0f3&vm_reference=VirtualMachine%3Avm-396
```

#### 正常返回示例
```
{
  "scode": 0,
  "desc": "",
  "message": "success",
  "message_cn": "成功",
  "stack": null,
  "data": {
    "name": "vm_040108",
    "reference": "VirtualMachine:vm-396",
    "overallStatus": "green",
    "powerState": "poweredOff",
    "host": "192.168.201.219",
    "guestMemUsage": 0,
    "annotation": "",
    "alarmActionsEnabled": true,
    "Mo": {
      "Self": {
        "Type": "VirtualMachine",
        "Value": "vm-396"
      },
      "Value": null,
      "AvailableField": null,
      "Parent": {
        "Type": "Folder",
        "Value": "group-v3"
      },
      "CustomValue": null,
      "OverallStatus": "green",
      "ConfigStatus": "green",
      "ConfigIssue": null,
      "EffectiveRole": [
        -1
      ],
      "Permission": null,
      "Name": "vm_040108",
      "DisabledMethod": [
        "MakePrimaryVM_Task",
        "TerminateFaultTolerantVM_Task",
        "ResetVM_Task",
        "UnmountToolsInstaller",
        "MountToolsInstaller",
        "MountToolsInstallerImage",
        "RebootGuest",
        "StandbyGuest",
        "ShutdownGuest",
        "PowerOffVM_Task",
        "ExtractOvfEnvironment",
        "SuspendVM_Task",
        "AcquireMksTicket",
        "AnswerVM",
        "UpgradeVM_Task",
        "UpgradeTools_Task",
        "UpgradeToolsFromImage_Task",
        "StartRecording_Task",
        "StopRecording_Task",
        "StartReplaying_Task",
        "StopReplaying_Task",
        "TurnOffFaultToleranceForVM_Task",
        "MakePrimaryVM_Task",
        "TerminateFaultTolerantVM_Task",
        "DisableSecondaryVM_Task",
        "EnableSecondaryVM_Task",
        "CreateSecondaryVM_Task",
        "CreateSecondaryVMEx_Task",
        "StopRecording_Task",
        "StopReplaying_Task",
        "MarkAsVirtualMachine"
      ],
      "RecentTask": [
        {
          "Type": "Task",
          "Value": "task-1105"
        },
        {
          "Type": "Task",
          "Value": "task-1106"
        },
        {
          "Type": "Task",
          "Value": "task-1107"
        },
        {
          "Type": "Task",
          "Value": "task-1108"
        },
        {
          "Type": "Task",
          "Value": "task-1109"
        },
        {
          "Type": "Task",
          "Value": "task-1110"
        },
        {
          "Type": "Task",
          "Value": "task-1111"
        }
      ],
      "DeclaredAlarmState": [
        {
          "Key": "alarm-10.vm-396",
          "Entity": {
            "Type": "VirtualMachine",
            "Value": "vm-396"
          },
          "Alarm": {
            "Type": "Alarm",
            "Value": "alarm-10"
          },
          "OverallStatus": "gray",
          "Time": "2019-04-08T13:07:19.208442Z",
          "Acknowledged": false,
          "AcknowledgedByUser": "",
          "AcknowledgedTime": null,
          "EventKey": 0
        },
        {
          "Key": "alarm-113.vm-396",
          "Entity": {
            "Type": "VirtualMachine",
            "Value": "vm-396"
          },
          "Alarm": {
            "Type": "Alarm",
            "Value": "alarm-113"
          },
          "OverallStatus": "gray",
          "Time": "2019-04-08T13:07:19.208442Z",
          "Acknowledged": false,
          "AcknowledgedByUser": "",
          "AcknowledgedTime": null,
          "EventKey": 0
        },
        {
          "Key": "alarm-12.vm-396",
          "Entity": {
            "Type": "VirtualMachine",
            "Value": "vm-396"
          },
          "Alarm": {
            "Type": "Alarm",
            "Value": "alarm-12"
          },
          "OverallStatus": "gray",
          "Time": "2019-04-08T13:07:19.208442Z",
          "Acknowledged": false,
          "AcknowledgedByUser": "",
          "AcknowledgedTime": null,
          "EventKey": 0
        },
        {
          "Key": "alarm-15.vm-396",
          "Entity": {
            "Type": "VirtualMachine",
            "Value": "vm-396"
          },
          "Alarm": {
            "Type": "Alarm",
            "Value": "alarm-15"
          },
          "OverallStatus": "gray",
          "Time": "2019-04-08T13:07:19.208442Z",
          "Acknowledged": false,
          "AcknowledgedByUser": "",
          "AcknowledgedTime": null,
          "EventKey": 0
        },
        {
          "Key": "alarm-19.vm-396",
          "Entity": {
            "Type": "VirtualMachine",
            "Value": "vm-396"
          },
          "Alarm": {
            "Type": "Alarm",
            "Value": "alarm-19"
          },
          "OverallStatus": "gray",
          "Time": "2019-04-08T13:07:19.208442Z",
          "Acknowledged": false,
          "AcknowledgedByUser": "",
          "AcknowledgedTime": null,
          "EventKey": 0
        },
        {
          "Key": "alarm-2.vm-396",
          "Entity": {
            "Type": "VirtualMachine",
            "Value": "vm-396"
          },
          "Alarm": {
            "Type": "Alarm",
            "Value": "alarm-2"
          },
          "OverallStatus": "gray",
          "Time": "2019-04-08T13:07:19.208442Z",
          "Acknowledged": false,
          "AcknowledgedByUser": "",
          "AcknowledgedTime": null,
          "EventKey": 0
        },
        {
          "Key": "alarm-38.vm-396",
          "Entity": {
            "Type": "VirtualMachine",
            "Value": "vm-396"
          },
          "Alarm": {
            "Type": "Alarm",
            "Value": "alarm-38"
          },
          "OverallStatus": "green",
          "Time": "2019-04-08T03:56:14.166999Z",
          "Acknowledged": false,
          "AcknowledgedByUser": "",
          "AcknowledgedTime": null,
          "EventKey": 16077
        },
        {
          "Key": "alarm-39.vm-396",
          "Entity": {
            "Type": "VirtualMachine",
            "Value": "vm-396"
          },
          "Alarm": {
            "Type": "Alarm",
            "Value": "alarm-39"
          },
          "OverallStatus": "gray",
          "Time": "2019-04-08T13:07:19.208442Z",
          "Acknowledged": false,
          "AcknowledgedByUser": "",
          "AcknowledgedTime": null,
          "EventKey": 0
        },
        {
          "Key": "alarm-40.vm-396",
          "Entity": {
            "Type": "VirtualMachine",
            "Value": "vm-396"
          },
          "Alarm": {
            "Type": "Alarm",
            "Value": "alarm-40"
          },
          "OverallStatus": "gray",
          "Time": "2019-04-08T13:07:19.208442Z",
          "Acknowledged": false,
          "AcknowledgedByUser": "",
          "AcknowledgedTime": null,
          "EventKey": 0
        },
        {
          "Key": "alarm-47.vm-396",
          "Entity": {
            "Type": "VirtualMachine",
            "Value": "vm-396"
          },
          "Alarm": {
            "Type": "Alarm",
            "Value": "alarm-47"
          },
          "OverallStatus": "gray",
          "Time": "2019-04-08T13:07:19.208442Z",
          "Acknowledged": false,
          "AcknowledgedByUser": "",
          "AcknowledgedTime": null,
          "EventKey": 0
        },
        {
          "Key": "alarm-5.vm-396",
          "Entity": {
            "Type": "VirtualMachine",
            "Value": "vm-396"
          },
          "Alarm": {
            "Type": "Alarm",
            "Value": "alarm-5"
          },
          "OverallStatus": "gray",
          "Time": "2019-04-08T13:07:19.208442Z",
          "Acknowledged": false,
          "AcknowledgedByUser": "",
          "AcknowledgedTime": null,
          "EventKey": 0
        },
        {
          "Key": "alarm-52.vm-396",
          "Entity": {
            "Type": "VirtualMachine",
            "Value": "vm-396"
          },
          "Alarm": {
            "Type": "Alarm",
            "Value": "alarm-52"
          },
          "OverallStatus": "gray",
          "Time": "2019-04-08T13:07:19.208442Z",
          "Acknowledged": false,
          "AcknowledgedByUser": "",
          "AcknowledgedTime": null,
          "EventKey": 0
        },
        {
          "Key": "alarm-54.vm-396",
          "Entity": {
            "Type": "VirtualMachine",
            "Value": "vm-396"
          },
          "Alarm": {
            "Type": "Alarm",
            "Value": "alarm-54"
          },
          "OverallStatus": "gray",
          "Time": "2019-04-08T13:07:19.208442Z",
          "Acknowledged": false,
          "AcknowledgedByUser": "",
          "AcknowledgedTime": null,
          "EventKey": 0
        },
        {
          "Key": "alarm-6.vm-396",
          "Entity": {
            "Type": "VirtualMachine",
            "Value": "vm-396"
          },
          "Alarm": {
            "Type": "Alarm",
            "Value": "alarm-6"
          },
          "OverallStatus": "gray",
          "Time": "2019-04-08T13:07:19.208442Z",
          "Acknowledged": false,
          "AcknowledgedByUser": "",
          "AcknowledgedTime": null,
          "EventKey": 0
        },
        {
          "Key": "alarm-81.vm-396",
          "Entity": {
            "Type": "VirtualMachine",
            "Value": "vm-396"
          },
          "Alarm": {
            "Type": "Alarm",
            "Value": "alarm-81"
          },
          "OverallStatus": "gray",
          "Time": "2019-04-08T13:07:19.208442Z",
          "Acknowledged": false,
          "AcknowledgedByUser": "",
          "AcknowledgedTime": null,
          "EventKey": 0
        },
        {
          "Key": "alarm-9.vm-396",
          "Entity": {
            "Type": "VirtualMachine",
            "Value": "vm-396"
          },
          "Alarm": {
            "Type": "Alarm",
            "Value": "alarm-9"
          },
          "OverallStatus": "gray",
          "Time": "2019-04-08T13:07:19.208442Z",
          "Acknowledged": false,
          "AcknowledgedByUser": "",
          "AcknowledgedTime": null,
          "EventKey": 0
        }
      ],
      "TriggeredAlarmState": null,
      "AlarmActionsEnabled": true,
      "Tag": null,
      "Capability": {
        "SnapshotOperationsSupported": true,
        "MultipleSnapshotsSupported": true,
        "SnapshotConfigSupported": true,
        "PoweredOffSnapshotsSupported": true,
        "MemorySnapshotsSupported": true,
        "RevertToSnapshotSupported": true,
        "QuiescedSnapshotsSupported": true,
        "DisableSnapshotsSupported": false,
        "LockSnapshotsSupported": true,
        "ConsolePreferencesSupported": false,
        "CpuFeatureMaskSupported": true,
        "S1AcpiManagementSupported": true,
        "SettingScreenResolutionSupported": false,
        "ToolsAutoUpdateSupported": false,
        "VmNpivWwnSupported": true,
        "NpivWwnOnNonRdmVmSupported": true,
        "VmNpivWwnDisableSupported": true,
        "VmNpivWwnUpdateSupported": true,
        "SwapPlacementSupported": true,
        "ToolsSyncTimeSupported": true,
        "VirtualMmuUsageSupported": false,
        "DiskSharesSupported": true,
        "BootOptionsSupported": true,
        "BootRetryOptionsSupported": true,
        "SettingVideoRamSizeSupported": true,
        "SettingDisplayTopologySupported": false,
        "RecordReplaySupported": false,
        "ChangeTrackingSupported": true,
        "MultipleCoresPerSocketSupported": true,
        "HostBasedReplicationSupported": true,
        "GuestAutoLockSupported": true,
        "MemoryReservationLockSupported": true,
        "FeatureRequirementSupported": true,
        "PoweredOnMonitorTypeChangeSupported": true,
        "SeSparseDiskSupported": true,
        "NestedHVSupported": true,
        "VPMCSupported": true,
        "SecureBootSupported": true,
        "PerVmEvcSupported": true,
        "VirtualMmuUsageIgnored": true,
        "VirtualExecUsageIgnored": true,
        "DiskOnlySnapshotOnSuspendedVMSupported": true
      },
      "Config": {
        "ChangeVersion": "2019-04-08T13:44:04.288396Z",
        "Modified": "1970-01-01T00:00:00Z",
        "Name": "vm_040108",
        "GuestFullName": "Microsoft Windows Server 2012 (64-bit)",
        "Version": "vmx-14",
        "Uuid": "4226e3fb-673d-d546-f043-a1d96521eee5",
        "CreateDate": "2019-04-01T09:25:37.864542Z",
        "InstanceUuid": "5026d9fb-3859-f68c-d843-02ab997b0549",
        "NpivNodeWorldWideName": null,
        "NpivPortWorldWideName": null,
        "NpivWorldWideNameType": "",
        "NpivDesiredNodeWwns": 0,
        "NpivDesiredPortWwns": 0,
        "NpivTemporaryDisabled": true,
        "NpivOnNonRdmDisks": null,
        "LocationId": "564d8ad4-59a2-a5d6-0c5b-c1dd75860441",
        "Template": false,
        "GuestId": "windows8Server64Guest",
        "AlternateGuestName": "",
        "Annotation": "",
        "Files": {
          "VmPathName": "[datastore1] vm_040108/vm_040108.vmx",
          "SnapshotDirectory": "[datastore1] vm_040108/",
          "SuspendDirectory": "[datastore1] vm_040108/",
          "LogDirectory": "[datastore1] vm_040108/",
          "FtMetadataDirectory": ""
        },
        "Tools": {
          "ToolsVersion": 0,
          "ToolsInstallType": "",
          "AfterPowerOn": true,
          "AfterResume": true,
          "BeforeGuestStandby": true,
          "BeforeGuestShutdown": true,
          "BeforeGuestReboot": null,
          "ToolsUpgradePolicy": "manual",
          "PendingCustomization": "",
          "CustomizationKeyId": null,
          "SyncTimeWithHost": false,
          "LastInstallInfo": {
            "Counter": 0,
            "Fault": null
          }
        },
        "Flags": {
          "DisableAcceleration": false,
          "EnableLogging": true,
          "UseToe": false,
          "RunWithDebugInfo": false,
          "MonitorType": "release",
          "HtSharing": "any",
          "SnapshotDisabled": false,
          "SnapshotLocked": false,
          "DiskUuidEnabled": true,
          "VirtualMmuUsage": "automatic",
          "VirtualExecUsage": "hvAuto",
          "SnapshotPowerOffBehavior": "powerOff",
          "RecordReplayEnabled": false,
          "FaultToleranceType": "unset",
          "CbrcCacheEnabled": false,
          "VvtdEnabled": false,
          "VbsEnabled": false
        },
        "ConsolePreferences": null,
        "DefaultPowerOps": {
          "PowerOffType": "soft",
          "SuspendType": "hard",
          "ResetType": "soft",
          "DefaultPowerOffType": "soft",
          "DefaultSuspendType": "hard",
          "DefaultResetType": "soft",
          "StandbyAction": "checkpoint"
        },
        "Hardware": {
          "NumCPU": 4,
          "NumCoresPerSocket": 1,
          "MemoryMB": 4096,
          "VirtualICH7MPresent": false,
          "VirtualSMCPresent": false,
          "Device": [
            {
              "Key": 200,
              "DeviceInfo": {
                "Label": "IDE 0",
                "Summary": "IDE 0"
              },
              "Backing": null,
              "Connectable": null,
              "SlotInfo": null,
              "ControllerKey": 0,
              "UnitNumber": null,
              "BusNumber": 0,
              "Device": null
            },
            {
              "Key": 201,
              "DeviceInfo": {
                "Label": "IDE 1",
                "Summary": "IDE 1"
              },
              "Backing": null,
              "Connectable": null,
              "SlotInfo": null,
              "ControllerKey": 0,
              "UnitNumber": null,
              "BusNumber": 1,
              "Device": null
            },
            {
              "Key": 300,
              "DeviceInfo": {
                "Label": "PS2 controller 0",
                "Summary": "PS2 controller 0"
              },
              "Backing": null,
              "Connectable": null,
              "SlotInfo": null,
              "ControllerKey": 0,
              "UnitNumber": null,
              "BusNumber": 0,
              "Device": [
                600,
                700
              ]
            },
            {
              "Key": 100,
              "DeviceInfo": {
                "Label": "PCI controller 0",
                "Summary": "PCI controller 0"
              },
              "Backing": null,
              "Connectable": null,
              "SlotInfo": null,
              "ControllerKey": 0,
              "UnitNumber": null,
              "BusNumber": 0,
              "Device": [
                500,
                12000
              ]
            },
            {
              "Key": 400,
              "DeviceInfo": {
                "Label": "SIO controller 0",
                "Summary": "SIO controller 0"
              },
              "Backing": null,
              "Connectable": null,
              "SlotInfo": null,
              "ControllerKey": 0,
              "UnitNumber": null,
              "BusNumber": 0,
              "Device": null
            },
            {
              "Key": 600,
              "DeviceInfo": {
                "Label": "Keyboard ",
                "Summary": "Keyboard"
              },
              "Backing": null,
              "Connectable": null,
              "SlotInfo": null,
              "ControllerKey": 300,
              "UnitNumber": 0
            },
            {
              "Key": 700,
              "DeviceInfo": {
                "Label": "Pointing device",
                "Summary": "Pointing device; Device"
              },
              "Backing": {
                "DeviceName": "",
                "UseAutoDetect": false,
                "HostPointingDevice": "autodetect"
              },
              "Connectable": null,
              "SlotInfo": null,
              "ControllerKey": 300,
              "UnitNumber": 1
            },
            {
              "Key": 500,
              "DeviceInfo": {
                "Label": "Video card ",
                "Summary": "Video card"
              },
              "Backing": null,
              "Connectable": null,
              "SlotInfo": null,
              "ControllerKey": 100,
              "UnitNumber": 0,
              "VideoRamSizeInKB": 12288,
              "NumDisplays": 2,
              "UseAutoDetect": false,
              "Enable3DSupport": true,
              "Use3dRenderer": "automatic",
              "GraphicsMemorySizeInKB": 262144
            },
            {
              "Key": 12000,
              "DeviceInfo": {
                "Label": "VMCI device",
                "Summary": "Device on the virtual machine PCI bus that provides support for the virtual machine communication interface"
              },
              "Backing": null,
              "Connectable": null,
              "SlotInfo": {
                "PciSlotNumber": 32
              },
              "ControllerKey": 100,
              "UnitNumber": 17,
              "Id": 1696722661,
              "AllowUnrestrictedCommunication": false,
              "FilterEnable": true,
              "FilterInfo": null
            }
          ]
        },
        "CpuAllocation": {
          "Reservation": 2300,
          "ExpandableReservation": false,
          "Limit": -1,
          "Shares": {
            "Shares": 1003,
            "Level": "custom"
          },
          "OverheadLimit": null
        },
        "MemoryAllocation": {
          "Reservation": 1244,
          "ExpandableReservation": false,
          "Limit": -1,
          "Shares": {
            "Shares": 40960,
            "Level": "normal"
          },
          "OverheadLimit": null
        },
        "LatencySensitivity": {
          "Level": "normal",
          "Sensitivity": 0
        },
        "MemoryHotAddEnabled": false,
        "CpuHotAddEnabled": false,
        "CpuHotRemoveEnabled": false,
        "HotPlugMemoryLimit": 0,
        "HotPlugMemoryIncrementSize": 0,
        "CpuAffinity": null,
        "MemoryAffinity": null,
        "NetworkShaper": null,
        "ExtraConfig": [
          {
            "Key": "nvram",
            "Value": "vm_040108.nvram"
          },
          {
            "Key": "pciBridge0.present",
            "Value": "TRUE"
          },
          {
            "Key": "svga.present",
            "Value": "TRUE"
          },
          {
            "Key": "pciBridge4.present",
            "Value": "TRUE"
          },
          {
            "Key": "pciBridge4.virtualDev",
            "Value": "pcieRootPort"
          },
          {
            "Key": "pciBridge4.functions",
            "Value": "8"
          },
          {
            "Key": "pciBridge5.present",
            "Value": "TRUE"
          },
          {
            "Key": "pciBridge5.virtualDev",
            "Value": "pcieRootPort"
          },
          {
            "Key": "pciBridge5.functions",
            "Value": "8"
          },
          {
            "Key": "pciBridge6.present",
            "Value": "TRUE"
          },
          {
            "Key": "pciBridge6.virtualDev",
            "Value": "pcieRootPort"
          },
          {
            "Key": "pciBridge6.functions",
            "Value": "8"
          },
          {
            "Key": "pciBridge7.present",
            "Value": "TRUE"
          },
          {
            "Key": "pciBridge7.virtualDev",
            "Value": "pcieRootPort"
          },
          {
            "Key": "pciBridge7.functions",
            "Value": "8"
          },
          {
            "Key": "hpet0.present",
            "Value": "TRUE"
          },
          {
            "Key": "svga.numDisplays",
            "Value": "2"
          },
          {
            "Key": "disk.EnableUUID",
            "Value": "TRUE"
          },
          {
            "Key": "mks.enable3d",
            "Value": "TRUE"
          },
          {
            "Key": "numa.autosize.cookie",
            "Value": "40001"
          },
          {
            "Key": "numa.autosize.vcpu.maxPerVirtualNode",
            "Value": "4"
          },
          {
            "Key": "sched.swap.derivedName",
            "Value": "/vmfs/volumes/5c2090bf-b3bc9996-fef9-5256ff008000/vm_040108/vm_040108-6b508014.vswp"
          },
          {
            "Key": "pciBridge0.pciSlotNumber",
            "Value": "17"
          },
          {
            "Key": "pciBridge4.pciSlotNumber",
            "Value": "21"
          },
          {
            "Key": "pciBridge5.pciSlotNumber",
            "Value": "22"
          },
          {
            "Key": "pciBridge6.pciSlotNumber",
            "Value": "23"
          },
          {
            "Key": "pciBridge7.pciSlotNumber",
            "Value": "24"
          },
          {
            "Key": "vmci0.pciSlotNumber",
            "Value": "32"
          },
          {
            "Key": "vm.genid",
            "Value": "1532788324642344444"
          },
          {
            "Key": "vm.genidX",
            "Value": "4144720387454556661"
          },
          {
            "Key": "monitor.phys_bits_used",
            "Value": "43"
          },
          {
            "Key": "vmotion.checkpointFBSize",
            "Value": "67108864"
          },
          {
            "Key": "vmotion.checkpointSVGAPrimarySize",
            "Value": "67108864"
          },
          {
            "Key": "softPowerOff",
            "Value": "FALSE"
          },
          {
            "Key": "tools.remindInstall",
            "Value": "TRUE"
          },
          {
            "Key": "vmware.tools.internalversion",
            "Value": "-1"
          },
          {
            "Key": "vmware.tools.requiredversion",
            "Value": "10304"
          },
          {
            "Key": "migrate.hostLogState",
            "Value": "none"
          },
          {
            "Key": "migrate.migrationId",
            "Value": "0"
          },
          {
            "Key": "migrate.hostLog",
            "Value": "vm_040108-07455552.hlog"
          }
        ],
        "CpuFeatureMask": null,
        "DatastoreUrl": [
          {
            "Name": "datastore1",
            "Url": "/vmfs/volumes/5c2090bf-b3bc9996-fef9-5256ff008000"
          }
        ],
        "SwapPlacement": "inherit",
        "BootOptions": {
          "BootDelay": 0,
          "EnterBIOSSetup": false,
          "EfiSecureBootEnabled": false,
          "BootRetryEnabled": false,
          "BootRetryDelay": 10000,
          "BootOrder": null,
          "NetworkBootProtocol": "ipv4"
        },
        "FtInfo": null,
        "RepConfig": null,
        "VAppConfig": null,
        "VAssertsEnabled": false,
        "ChangeTrackingEnabled": false,
        "Firmware": "efi",
        "MaxMksConnections": 40,
        "GuestAutoLockEnabled": false,
        "ManagedBy": null,
        "MemoryReservationLockedToMax": false,
        "InitialOverhead": {
          "InitialMemoryReservation": 132448256,
          "InitialSwapReservation": 1374314496
        },
        "NestedHVEnabled": false,
        "VPMCEnabled": false,
        "ScheduledHardwareUpgradeInfo": {
          "UpgradePolicy": "never",
          "VersionKey": "",
          "ScheduledHardwareUpgradeStatus": "none",
          "Fault": null
        },
        "ForkConfigInfo": null,
        "VFlashCacheReservation": 0,
        "VmxConfigChecksum": "d2lFOHErZzBUankrUXJjK2Y4Y3R4Mmg0cExRPQ==",
        "MessageBusTunnelEnabled": false,
        "VmStorageObjectId": "",
        "SwapStorageObjectId": "",
        "KeyId": null,
        "GuestIntegrityInfo": {
          "Enabled": false
        },
        "MigrateEncryption": "opportunistic"
      },
      "Layout": {
        "ConfigFile": [
          "vm_040108.nvram",
          "vm_040108.vmsd"
        ],
        "LogFile": [
          "vmware.log"
        ],
        "Disk": null,
        "Snapshot": null,
        "SwapFile": ""
      },
      "LayoutEx": {
        "File": [
          {
            "Key": 0,
            "Name": "[datastore1] vm_040108/vm_040108.vmx",
            "Type": "config",
            "Size": 0,
            "UniqueSize": 0,
            "BackingObjectId": "",
            "Accessible": true
          },
          {
            "Key": 1,
            "Name": "[datastore1] vm_040108/vm_040108.nvram",
            "Type": "nvram",
            "Size": 270840,
            "UniqueSize": 270840,
            "BackingObjectId": "",
            "Accessible": true
          },
          {
            "Key": 2,
            "Name": "[datastore1] vm_040108/vm_040108.vmsd",
            "Type": "snapshotList",
            "Size": 0,
            "UniqueSize": 0,
            "BackingObjectId": "",
            "Accessible": true
          },
          {
            "Key": 3,
            "Name": "[datastore1] vm_040108/vmware.log",
            "Type": "log",
            "Size": 176920,
            "UniqueSize": 176920,
            "BackingObjectId": "",
            "Accessible": true
          }
        ],
        "Disk": null,
        "Snapshot": null,
        "Timestamp": "2019-04-08T13:45:19.278489Z"
      },
      "Storage": {
        "PerDatastoreUsage": [
          {
            "Datastore": {
              "Type": "Datastore",
              "Value": "datastore-10"
            },
            "Committed": 447760,
            "Uncommitted": 4364853248,
            "Unshared": 0
          }
        ],
        "Timestamp": "2019-04-08T13:18:05.985Z"
      },
      "EnvironmentBrowser": {
        "Type": "EnvironmentBrowser",
        "Value": "envbrowser-396"
      },
      "ResourcePool": {
        "Type": "ResourcePool",
        "Value": "resgroup-8"
      },
      "ParentVApp": null,
      "ResourceConfig": {
        "Entity": {
          "Type": "VirtualMachine",
          "Value": "vm-396"
        },
        "ChangeVersion": "",
        "LastModified": null,
        "CpuAllocation": {
          "Reservation": 2300,
          "ExpandableReservation": false,
          "Limit": -1,
          "Shares": {
            "Shares": 1003,
            "Level": "custom"
          },
          "OverheadLimit": null
        },
        "MemoryAllocation": {
          "Reservation": 1244,
          "ExpandableReservation": false,
          "Limit": -1,
          "Shares": {
            "Shares": 40960,
            "Level": "normal"
          },
          "OverheadLimit": null
        }
      },
      "Runtime": {
        "Device": null,
        "Host": {
          "Type": "HostSystem",
          "Value": "host-9"
        },
        "ConnectionState": "connected",
        "PowerState": "poweredOff",
        "FaultToleranceState": "notConfigured",
        "DasVmProtection": null,
        "ToolsInstallerMounted": false,
        "SuspendTime": null,
        "BootTime": null,
        "SuspendInterval": 0,
        "Question": null,
        "MemoryOverhead": 0,
        "MaxCpuUsage": 0,
        "MaxMemoryUsage": 0,
        "NumMksConnections": 0,
        "RecordReplayState": "inactive",
        "CleanPowerOff": null,
        "NeedSecondaryReason": "",
        "OnlineStandby": false,
        "MinRequiredEVCModeKey": "",
        "ConsolidationNeeded": false,
        "OfflineFeatureRequirement": [
          {
            "Key": "cpuid.lm",
            "FeatureName": "cpuid.lm",
            "Value": "Bool:Min:1"
          }
        ],
        "FeatureRequirement": null,
        "FeatureMask": null,
        "VFlashCacheAllocation": 0,
        "Paused": false,
        "SnapshotInBackground": false,
        "QuiescedForkParent": null,
        "InstantCloneFrozen": false,
        "CryptoState": ""
      },
      "Guest": {
        "ToolsStatus": "toolsNotInstalled",
        "ToolsVersionStatus": "",
        "ToolsVersionStatus2": "",
        "ToolsRunningStatus": "guestToolsNotRunning",
        "ToolsVersion": "",
        "ToolsInstallType": "",
        "GuestId": "windows8Server64Guest",
        "GuestFamily": "",
        "GuestFullName": "Microsoft Windows Server 2012 (64-bit)",
        "HostName": "",
        "IpAddress": "",
        "Net": null,
        "IpStack": null,
        "Disk": null,
        "Screen": {
          "Width": 0,
          "Height": 0
        },
        "GuestState": "notRunning",
        "AppHeartbeatStatus": "",
        "GuestKernelCrashed": false,
        "AppState": "",
        "GuestOperationsReady": false,
        "InteractiveGuestOperationsReady": false,
        "GuestStateChangeSupported": false,
        "GenerationInfo": null
      },
      "Summary": {
        "Vm": {
          "Type": "VirtualMachine",
          "Value": "vm-396"
        },
        "Runtime": {
          "Device": null,
          "Host": {
            "Type": "HostSystem",
            "Value": "host-9"
          },
          "ConnectionState": "connected",
          "PowerState": "poweredOff",
          "FaultToleranceState": "notConfigured",
          "DasVmProtection": null,
          "ToolsInstallerMounted": false,
          "SuspendTime": null,
          "BootTime": null,
          "SuspendInterval": 0,
          "Question": null,
          "MemoryOverhead": 0,
          "MaxCpuUsage": 0,
          "MaxMemoryUsage": 0,
          "NumMksConnections": 0,
          "RecordReplayState": "inactive",
          "CleanPowerOff": null,
          "NeedSecondaryReason": "",
          "OnlineStandby": false,
          "MinRequiredEVCModeKey": "",
          "ConsolidationNeeded": false,
          "OfflineFeatureRequirement": [
            {
              "Key": "cpuid.lm",
              "FeatureName": "cpuid.lm",
              "Value": "Bool:Min:1"
            }
          ],
          "FeatureRequirement": null,
          "FeatureMask": null,
          "VFlashCacheAllocation": 0,
          "Paused": false,
          "SnapshotInBackground": false,
          "QuiescedForkParent": null,
          "InstantCloneFrozen": false,
          "CryptoState": ""
        },
        "Guest": {
          "GuestId": "windows8Server64Guest",
          "GuestFullName": "Microsoft Windows Server 2012 (64-bit)",
          "ToolsStatus": "toolsNotInstalled",
          "ToolsVersionStatus": "",
          "ToolsVersionStatus2": "",
          "ToolsRunningStatus": "guestToolsNotRunning",
          "HostName": "",
          "IpAddress": ""
        },
        "Config": {
          "Name": "vm_040108",
          "Template": false,
          "VmPathName": "[datastore1] vm_040108/vm_040108.vmx",
          "MemorySizeMB": 4096,
          "CpuReservation": 2300,
          "MemoryReservation": 1244,
          "NumCpu": 4,
          "NumEthernetCards": 0,
          "NumVirtualDisks": 0,
          "Uuid": "4226e3fb-673d-d546-f043-a1d96521eee5",
          "InstanceUuid": "5026d9fb-3859-f68c-d843-02ab997b0549",
          "GuestId": "windows8Server64Guest",
          "GuestFullName": "Microsoft Windows Server 2012 (64-bit)",
          "Annotation": "",
          "Product": null,
          "InstallBootRequired": false,
          "FtInfo": null,
          "ManagedBy": null,
          "TpmPresent": false,
          "NumVmiopBackings": 0
        },
        "Storage": {
          "Committed": 447760,
          "Uncommitted": 4364853248,
          "Unshared": 0,
          "Timestamp": "2019-04-08T13:18:05.98552Z"
        },
        "QuickStats": {
          "OverallCpuUsage": 0,
          "OverallCpuDemand": 0,
          "GuestMemoryUsage": 0,
          "HostMemoryUsage": 0,
          "GuestHeartbeatStatus": "gray",
          "DistributedCpuEntitlement": 0,
          "DistributedMemoryEntitlement": 0,
          "StaticCpuEntitlement": 0,
          "StaticMemoryEntitlement": 0,
          "PrivateMemory": 0,
          "SharedMemory": 0,
          "SwappedMemory": 0,
          "BalloonedMemory": 0,
          "ConsumedOverheadMemory": 0,
          "FtLogBandwidth": -1,
          "FtSecondaryLatency": -1,
          "FtLatencyStatus": "gray",
          "CompressedMemory": 0,
          "UptimeSeconds": 0,
          "SsdSwappedMemory": 0
        },
        "OverallStatus": "green",
        "CustomValue": null
      },
      "Datastore": [
        {
          "Type": "Datastore",
          "Value": "datastore-10"
        }
      ],
      "Network": null,
      "Snapshot": null,
      "RootSnapshot": null,
      "GuestHeartbeatStatus": "gray"
    },
    "memUsage": 0,
    "diskTotal": 447760,
    "diskFree": 4364853248,
    "Networks": null,
    "Datastores": null,
    "HostSystenReference": "HostSystem:host-9"
  }
}
```

#### 异常返回示例

### 状态码