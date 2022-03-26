**AWS Lambda**

    AWS Lambda is an event-driven serverless computing cloud service from Amazon Web Services that allows developers to program functions on a pay-per-use basis without creating, managing or paying for servers.
    
    AWS lambda also know as function-as-a-Service (FaaS).

    We just need to write our code and lambda function will automatically trigger execution by receiving some event. 

    We can write our code in python, java , c++, ruby or javascript.

    Aws lambda mostly use to deploy background task and not for any heavy applications of because of certain limitations. 
    
    Aws lambda not only exeutes your code but also manages resources as per the workload size. We only need to pay for the compute time. 

    Lambda is best suited for shorter, event-driven workloads, since Lambda functions run for up to 15 minutes per invocation. 

    We can invoke lambda using lambda API or using some event from other aws services. 

**AWS Lambda limitations**

    1. Payload Size : 
        Lambda payloads (whether invoked by HTTP request or other means) have a limit of 6 MB. When running Lambda behind API Gateway or a load balancer, this means you need to make sure your HTTP requests are small.For the most part, this means not managing file uploads in the application directly. Instead, you can upload files directly to an S3 bucket (and then send a request to your application that has the location of the uploaded file).

    2. Execution Time : 
        Lambdas have a hard limit on execution time. After 15 minutes, your function will be stopped whether it’s finished or not. If this is a problem, then AWS Lambdas and functions-as-a-service aren’t a good fit for your application.
    
    3. Read Only Access : 
        Lambda file systems are read-only, with the exception of the /tmp directory. That directory has a storage limit of 512 MB. The file systems are not persistent - you'll lose any filesystem based changes (new files, changed files, etc). You absolutely cannot expect files to exist between invocations of Lambda functions.
        This means that any persistence needs to be handled outside of Lambda. Files can be uploaded to, or downloaded from, S3 as needed.
        A file managed within a Lambda function can be stored in-memory for a program to work on, or saved to the /tmp directory. RAM limits and the /tmp directory size limit are the limiting factors in those scenarios.
        You determine how much RAM/CPU us available to a Lambda function ahead of time. This is part of the pricing model for Lambda.
        Databases, caches, etc, will all need to be hosted elsewhere. Using a managed service such as DynamoDB, RDS, or ElastiCache is the most common way to accomplish this.
        If you need to store files that never change in your Lambda function, you can use Layers to add that data into the Lambda function.You can also attach EFS drives to your Lambda function, allowing for persistent file storage.
    
    4. Concurrency :
    
    5. Deployment Package Size :
        Building Lambda functions involves packaging your code, either as a .zip file or a container image.If you're uploading files as your Lambda function, there's a limit of 50 MB for the ZIP file and 250 MB for the unzipped files. Functions packaged as a container image have a much larger limit - 10 GB!. Container images are the way to build your Lambda functions if you're in danger of hitting size limits.
    
    6. Cold Start :
        Lambda functions have the concept of a Cold Start.Essentially, AWS needs to download the Lambda function and start its execution environment. This takes time! That time isn't billed for, but certainly adds time to the response time.
        After a function is "warmed", it stays running for a period of time (to potentially handle additional requests) for a varying amount of time.The potential delay due to cold start times is felt the most for HTTP requests, where a user might be waiting on a response in real time.
        There are two ways to reduce cold start times:
        
        1. Warming Requests - EventBridge (formerly "CloudWatch Events") can be configured to send a request to your Lambda function once per minute to keep it warm. This isn't perfect - it increases the likelihood an HTTP request won't hit a cold start, rather than guarantees it.

        2. Provisioned Concurrency - Pay to have Lambda functions warmed and ready to accept new requests (more on that here)


**Imp links**

    https://dashbird.io/blog/machine-learning-in-aws-lambda/
    https://aws.amazon.com/blogs/compute/operating-lambda-performance-optimization-part-1/
    https://aws.amazon.com/blogs/compute/new-for-aws-lambda-predictable-start-up-times-with-provisioned-concurrency/