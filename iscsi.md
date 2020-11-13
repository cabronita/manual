### iscsi client

Install package

`yum install -y iscsi-initiator-utils`

Print `INITIATOR_NAME`

`awk -F= '{print $NF}' /etc/iscsi/initiatorname.iscsi`

### iscsi server

Install package

`yum install -y targetcli`

Enable service

`systemctl enable --now target`

Create `LUN`

`targetcli /backstores/block create dev=$LUN name=lun0`

Create target

`targetcli /iscsi create iqn.2003-01.org.linux-iscsi.$(hostname -s):lun0`

Set ACL for `INITIATOR_NAME`

`targetcli /iscsi/iqn.2003-01.org.linux-iscsi.$(hostname -s):lun0/tpg1/acls create wwn=$INITIATOR_NAME`

Create reference to `LUN`

`targetcli /iscsi/iqn.2003-01.org.linux-iscsi.$(hostname -s):lun0/tpg1/luns create /backstores/block/lun0`

Save config

`targetcli saveconfig`

### iscsi client

Discover target on `SERVER`

`iscsiadm -m discovery -t sendtargets -p $SERVER`

Log in to the discovered target

`iscsiadm -m node -T iqn.2003-01.org.linux-iscsi.$SERVER:lun0 -l`

or

`iscsiadm -m node -l`
