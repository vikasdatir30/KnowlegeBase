**To generate SSK keys**
    
    open git-bash and type 
    ssh-keygen -t rsa -b 4096 -C "datir.vikas@outlook.com"
    
    enter password and you will get public and private keys
    under .ssh folder in user folder 
    
    --run 
    eval $(ssh-agent -s)

    --add private key 
    ssh-add id_rsa

    --copy public key and add to the git hub account 
    clip < id_ras.pub


https://www.youtube.com/watch?v=-U-eUHI6euM&list=PLhW3qG5bs-L8OlICbNX9u4MZ3rAt5c5GG&ab_channel=AutomationStepbyStep

**Git Basic**


    Git - vcs version control system 
        - helps us to track chnages and updated to each and every file 
        - to collabrates with teams
    
    There are two types of VCS
    1. Centerialize VCS
    2. Distributed VCS - Git - free and open source 

    GitHub  - a platform to uplaod and host your repository 
            - provides back up 
            - provides visual interface 
            - make collaboration easier 
  
    Git and GitHUB are not same .. Git!= GitHub





    

