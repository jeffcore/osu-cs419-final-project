The following tools have been posted to this folder:
	sql_cmd.py
	mysql419.py

These tools must be run from an engineering server (e.g. FLIP).

<Tool> sql_cmd.py

	This tool implements a MySQL command on the CS419 group8 database.
	It is a self-contained function meant to be called by other scripts.

	To use this tool within another python script: 
		import sql_cmd
		syntax: 'sql_cmd.execute(query)' where query = MySQL query text string
		example: assigning sql_cmd result to variable sql_result:
			sql_result = sql_cmd.execute(query)

<Tool> mysql419.py

	To RUN this tool, type at the command prompt:
		python mysql419.py

	This tool emulates a live MySQL console applied to the cs419-g8 database.
	At runtime, user gets a prompt 'mysql419 >> '
	Enter a MySQL query at the prompt.

	Any input containing ';' will mark the end of a query and be executed.
	Until an input contains ';' any new text is added to a query being constructed.
	You may add multi-line queries and multiple queries at the same time.  The 
	program will execute the queries sequentially.

	To EXIT, enter 'exit' at the prompt.

<EXAMPLE> Below is text from Linux command line session using mysql419.py

	flip3 ~/CS419 22% python mysql419.py
	mysql419 >>show databases;
	USE cs419-g8;
	SET FOREIGN_KEY_CHECKS=0;
	DROP TABLE IF EXISTS 'test_create_table';
	CREATE TABLE 'test_create_table'(
	'id' INT(11) AUTO_INCREMENT,
	'name' VARCHAR(255),
	PRIMARY KEY ('id')
	) ENGINE=InnoDB;
	show tables;

	(query >> 'show databases;')
	+--------------------+
	| Database           |
	+--------------------+
	| information_schema |
	| cs419-g8           |
	+--------------------+

	mysql419 >>(query >> 'USE cs419-g8;')

	mysql419 >>(query >> 'SET FOREIGN_KEY_CHECKS=0;')

	mysql419 >>(query >> 'DROP TABLE IF EXISTS 'test_create_table';')

	mysql419 >>>>>>>>>>(query >> 'CREATE TABLE 'test_create_table'('id' INT(11) AUTO_INCREMENT,'name' VARCHAR(255),PRIMARY KEY ('id')) ENGINE=InnoDB;')

	mysql419 >>(query >> 'show tables;')
	+--------------------+
	| Tables_in_cs419-g8 |
	+--------------------+
	| test_create_table  |
	+--------------------+

	mysql419 >>SHOW CREATE TABLE 'test_create_table';
	(query >> 'SHOW CREATE TABLE 'test_create_table';')
	+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| Table             | Create Table                                                                                                                                                               |
	+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
	| test_create_table | CREATE TABLE `test_create_table` (
	  `id` int(11) NOT NULL AUTO_INCREMENT,
	  `name` varchar(255) DEFAULT NULL,
	  PRIMARY KEY (`id`)
	) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
	+-------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

	mysql419 >>SHOW COLUMNS IN 'test_create_table';
	(query >> 'SHOW COLUMNS IN 'test_create_table';')
	+-------+--------------+------+-----+---------+----------------+
	| Field | Type         | Null | Key | Default | Extra          |
	+-------+--------------+------+-----+---------+----------------+
	| id    | int(11)      | NO   | PRI | NULL    | auto_increment |
	| name  | varchar(255) | YES  |     | NULL    |                |
	+-------+--------------+------+-----+---------+----------------+

	mysql419 >>SHOW COLUMNS FROM 'test_create_table';
	(query >> 'SHOW COLUMNS FROM 'test_create_table';')
	+-------+--------------+------+-----+---------+----------------+
	| Field | Type         | Null | Key | Default | Extra          |
	+-------+--------------+------+-----+---------+----------------+
	| id    | int(11)      | NO   | PRI | NULL    | auto_increment |
	| name  | varchar(255) | YES  |     | NULL    |                |
	+-------+--------------+------+-----+---------+----------------+

	mysql419 >>SELECT * FROM 'test_create_table';
	(query >> 'SELECT * FROM 'test_create_table';')

	mysql419 >>INSERT INTO 'test_create_table' ('name') VALUES ("Kevin McGrath");
	(query >> 'INSERT INTO 'test_create_table' ('name') VALUES ("Kevin McGrath");')

	mysql419 >>SELECT * FROM 'test_create_table';
	(query >> 'SELECT * FROM 'test_create_table';')
	+----+---------------+
	| id | name          |
	+----+---------------+
	|  1 | Kevin McGrath |
	+----+---------------+

	mysql419 >>exit
	flip3 ~/CS419 23% 

