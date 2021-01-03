
將儲存在Mysql的網路設備資料，透過Django使用網頁呈現出來，net為Django的一個project，my為Django的一個app。
一個區網內有許多設備，每個設備設定固定IP，想要找出每個設備連接的網路設備與網路設備的連接埠，需要事先連線到交換器(Switch)查詢MAC所對應的交換器連接埠，例如：MAC(01:02:03:04:05:06)連結Switch(代號為lib-4F-1)的port2，此時就可以建立一個資料表儲存MAC、Switch代號與Switc連接埠，如下。

 MAC       |         Switch	 |   Port
 
 01:02:03:04:05:06	| lib-4F-1	| 2
 
 在Linux或FreeBSD使用指令「arp-scan」 ，掃描區域網路內所有IP、MAC、機器型號等對應，如下。
 
 IP      |      MAC	        |       Com
 
 192.168.1.1	|  01:02:03:04:05:06	|ASUS
 
 事先將這些資料插入Mysql資料庫，並使用Django連線Mysql資料庫，使用Django建立查詢兩張資料表，使用MAC連結兩張資料表，找出區往IP、MAC、交換器(Switch)、交換器連接埠(Port)與機器型號(Com)，使用網頁呈現出來，可以呈現一整個Vlan、一個區間的IP或單一個IP的資訊。
