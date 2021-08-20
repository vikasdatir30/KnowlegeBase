


























****
**Streams and Tasks**

*Streams*
    
    Streams are used to implemment CDC functionality in the snowflake.
    Streams objects are associated with the source table which tracks DML operation like insert, update ordelete
    Whenever data in inserted, deleted or updated streams object hold that data (delta load).
    When we create stream object it add three new fields to the table 
        1. metadata$action
        2. metadata$isupdate
        3. metadata$rowid
    Using these column we can track the DML changes. 
    
    example
    create or replace stream test_db.public.sales_raw_stream 
    on test_db.public.sales_raw

    There are 3 types of streams 
    Standard
    Append-only 
    Insert-only

*Tasks*

    Using task object we can shedule the excution of the sql statement.
    A task can execute single sql statement which may inculdes - a call to the stored procedure.
    There is no event source that can trigger the task we need to specify the trigger event to that task will start the execution. 
    

**Example**
    
    use role sysadmin; 
    use warehouse compute_wh;
    use database test_db;
    use schema public;
    
    --level-0
    -- external table acts as source 
    create table test_db.public.user_ext(
    full_name string,
    email_id string,
    year string);

    create or replace file format csv_file_format 
    type ='csv',
    compression='auto',
    field_delimiter= ',',
    record_delimiter= '\n';

    create or replace stage user_ext_stage 
    file_format= csv_file_format;

    --loaded data into user_ext table 
    select * from user_ext;

    -- level-1
    create or replace table user_raw (
    user_name varchar(100),
    email_id  varchar(100),
    year int
    );

    insert into user_raw 
    select * from user_ext;

    create or replace stream user_raw_stream
    on table user_raw
    comment="stream to handle chnaged data";

    create or replace task user_raw_task
    warehouse = compute_wh
    schedule =  '1 minute'
    when 
    system$stream_has_data('test_db.public.user_raw_stream')
    as
    insert into user_final(first_name, last_name, email_id , year )
    select replace(split(user_name ,' ')[0],'"','') as first_name ,
    replace(split(user_name ,' ')[1],'"','') as last_name ,
    email_id , year
    from user_raw_stream;

    use role sysadmin;
    alter task user_raw_task resume;

    show grants to role sysadmin; 

    use role accountadmin ;

    grant EXECUTE TASK to role sysadmin;

    show streams;
    select  * from user_raw_stream;
    select * from user_raw;

    describe table user_raw;
    describe stream user_raw_stream;
    describe task user_raw_task;

    --level-2
    create or replace sequence user_id_seq start =1 increment=1 ;

    create or replace table user_final (
    user_id number default user_id_seq.nextval,
    first_name varchar(100),
    last_name varchar(100),
    email_id varchar(100), 
    year int);

    insert into user_final(first_name, last_name, email_id , year )
    select replace(split(user_name ,' ')[0],'"','') as first_name ,
    replace(split(user_name ,' ')[1],'"','') as last_name ,
    email_id , year
    from user_raw_stream;

    select * from user_final;



