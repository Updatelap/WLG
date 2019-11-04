# WLG
## Word-List Token Generator &amp; Filter used to hack FB account 

Impact
===
[1]. Full Account Takeover using SMS Recovery Code.

       Poc Ex: 
       https://fb.me/XXXXXXXXXXXXXX -> 301 -> https://m.facebook.com/n/?recover%2Fcode%2F&u=100002271816418&n=711180&aref=XXX&medium=sms&mid=XXX&n_m=%2B962799999999

[2]. Business Account Takeover using invitations Token.

       Poc Ex: 
       https://fb.me/XXXXXXXXXXXXXX -> 301 -> https://business.facebook.com/invitation/?token=Invite-Token

[3]. CSRF Attack based GET Request leads to Turn OFF "SMS messages".

       Poc Ex: 
       https://fb.me/XXXXXXXXXXXXXX -> 301 -> https://www.facebook.com/settings/sms/phone_prefs_opt_out/?user_id=100002271816418&phone=%2B962799999999&token=XXXXXXXXXXXXXXXX

[3]. Information disclosure: 

      A  Phone Number
           Poc Ex: 
          https://fb.me/XXXXXXXXXXXXXX -> 301 -> https://www.facebook.com/settings/sms/phone_prefs_opt_out/?user_id=100002271816418&phone=%2B962799999999&token=XXXXXXXXXXXXXXXX

      B.  Business info leaks 
            businessID 
            businessName
            businessAdmin 
            Email invited
            PoC Ex: 
            https://fb.me/XXXXXXXXXXXXXX -> 301 -> https://business.facebook.com/invitation/?token=Invite-Token

![](https://github.com/Updatelap/WLG/blob/master/Bug_ATO_FB.png)



### Coded By [@Jafar_Abu_Nada](https://twitter.com/Jafar_Abu_Nada)
