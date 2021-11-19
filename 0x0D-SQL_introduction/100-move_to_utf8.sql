-- Convert 'hbtn_0c_0' to utf8mb4, collate utf8mb4_unicode_ci               
-- Convert db 'hbtn_0c_0'                                                   
USE hbtn_0c_0
-- convert DB                                                                
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- convert first_table                                                      
ALTER TABLE first_table	CONVERT	TO CHARACTER SET utf8mb4 COLLATE utf8mb4_un\
icode_ci;
-- convert name field                                                       
ALTER TABLE first_table	MODIFY name VARCHAR(256) CHARACTER SET utf8mb4;
