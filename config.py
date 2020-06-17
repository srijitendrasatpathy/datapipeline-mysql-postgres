# import os

# For additonal security you could add the credentials in the environment variables and read it as below.


# MYSQL_DB_USER=os.environ.get('MYSQL_DB_USER')
# MYSQL_DB_PASS=os.environ.get('MYSQL_DB_PASS')

# PROSTGES_DB_USER=os.environ.get('PROSTGES_DB_USER')
# PROSTGES_DB_PASS=os.environ.get('PROSTGES_DB_USER')

DB_DETAILS = {
    
    'SOURCE_DB':{
        'DB_TYPE':'mysql',
        'DB_HOST':'127.0.0.1',
        'DB_NAME':'retail_db',
        'DB_USER':'mysql_user',
        'DB_PASS':'password'

    },
    'TARGET_DB' :{
        'DB_TYPE':'psotgres',
        'DB_HOST':'127.0.0.1',
        'DB_NAME':'retail_db',
        'DB_USER':'target_user',
        'DB_PASS':'password'
    }
}