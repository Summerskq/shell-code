#!/usr/bin/expect
set ip [ lindex $argv 0 ]
set passwd [ lindex $argv 1 ]
spawn ssh root@$ip
expect {
	"(yes/no)?" { send "yes\n"}
	"passwd:" {send "$passwd\n"}
}
interact
