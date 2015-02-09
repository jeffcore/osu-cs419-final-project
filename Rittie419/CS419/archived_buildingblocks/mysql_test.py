import subprocess
import sql_cmd

query = '''
show databases;
USE cs419-g8;
SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS 'test_create_table';
CREATE TABLE 'test_create_table'(
'id' INT(11) AUTO_INCREMENT,
'name' VARCHAR(255),
PRIMARY KEY ('id')
) ENGINE=InnoDB;
show tables;

'''
linux_cmd = "mysql -u cs419-g8 --password=9bWxwfvCAqUncYZV -t -e '%s' -h mysql.eecs.oregonstate.edu" % query

output = subprocess.Popen(linux_cmd, shell=True, stdout=subprocess.PIPE).communicate()[0]

print linux_cmd
print output

print sql_cmd.execute('show tables;')
'''
show databases;
USE cs419-g8;
SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS 'test_create_table';
CREATE TABLE 'test_create_table'(
'id' INT(11) AUTO_INCREMENT,
PRIMARY KEY ('id')
) ENGINE=InnoDB;
show tables;

INSERT INTO 'test_create_table' ('name') VALUES ("Kevin McGrath");
SHOW CREATE TABLE 'test_create_table';
SHOW COLUMNS IN 'test_create_table';
SHOW COLUMNS FROM 'test_create_table';
SELECT * FROM 'test_create_table';

'''
