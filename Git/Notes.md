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

    to check version 
    git --version 

**Configure Git**

    on terminal 
    setp-1 
    git config --global user.name "user_name"
    git config --global user.email "user_email"

    step-2
    create one folder and go to that folder in terminal 
    eg : E:\Data\TestGit
    on terminal 
    cd E:\Data\TestGit
    git init


    step-3:Setting Repo with GitHub
    go to the github account and create a repository 
    go to terminal and execute 
    git remote add origin <URL_of_repo>

    to push files to master branch 
    git push -u origin master 


    commands
    git status
    git add <file_name>
    git commit -m "message" <file_name>
    git log 
    git --help 
    
**Branchin and Merging**

    Step 1 : create a branch 
    git branch <branch_name>
    
    this will create new branch but you need to move from master branch into newly created branch for that you need to execute 

    Step 2: checkout branch 
    git checkout <branch_name>
    
    using this command you are in a newly created branch 
    
    step 3: Add your file or modify and commit it 
    git add <file_name>
    git commit -m  "msg" <file_name>

    setp 4: Push changes to the branch on github
    git push -u origin <branch_name>
    
    After this you will see new branches on the github repo
    
    Step 5: merging 
    To merge branch first you need to checkout the master branch 
    
    git checkout master 
    git merge <branch_name>

    step 6: pushing merge to git hub 
    once you merged branch at local repo you can push those chnages to github 
    
    git push -u origin master 

    step 7: deleting branch 
    once you merged branch with master you can delete branch using below command 
    
    git branch -d <branch_name>  

    this command will delete branch at local repo if you want to delete branch from remote github location 
    
    git push origin --delete <branch_name>


**Email Notification for change**

    Step 1 : go to the repository on github and select repository
    step 2 : go to the setting option --> integration and services menu --> add service 
    step 3 : select email option from dropdown list and add your email Id  

    once you added your email .. then whenever any chnages happen at repository you will get notification email 

    
**Git TAG**

    Git Tag are points in history for your repository 
    It is mostly used for release points, for example when your project is stable and you want to do marking then you can use taging 
    like v1.0, v1.1 etc 

    Use : 
    - Tag helps us to mark our release points for our code/data when our project is stable 
    - Using tag you can also create historic restore point 

    When to use :
    - When you want to create a release point for stable version of your code 
    - To create historic restore point for future use 

    Steps to create tags 
    step 1 : check out the branch where you want to create the tag 
    
    git checkout <branch_name>
    ex : git checkout master 

    step 2 :  create tag 
    git tag <tag_name>
    git tag v1.0
    
    to check tag use 
    git tag 
    
    Using this you can have light weight tag, this tag will not save any other information like creator of the tag etc 
    
    Annotated TAG: to create annotated tag you can use below command 
    
    git tag -a <tag_name> -m "message for tag "
    git tag -a v1.1 -m "tag for release ver 1.1"

    In annotated tag you can give the message and contain information about the tagger. it also saved as object in git. 

    step 3: To show tag use below commands :
    git tag 
    git show <tag_name>

    git tag -l "v1.*" -- display all the tag starting with v1.
    
    How to push tag to Remote repo :
    to push your tag on remote repository use the below command 
    
    git push origin <tag_name>
    git push origin v1.0 
    git push origin --tags
    git push --tags : this will push all tags 

    How to delete tags : 
    git tag -d <tag_name> : this will delete tag from local 
    git push origin -delete <tag_name>  : this will delete tag from remote repo 

    Real life use of tags : 
    In development environment you can have multiple branches and tag. if you want to work on specific release let for modification or want to add new feature then using tag you can create new branch. You can use below command to create new branch from the tag.

    git checkout -b <branch_name> <tag_name>

    Also you can create tag for specific past commit operation. 
    git tag <tag_name> <checksum_number_for_past_commit>

**Extras**


    When you commit any changes git generate a unique 14 digit number this number is called checksum. 
    This number is associated with each commit operation. You can view checksum number using [git log] command 













    

