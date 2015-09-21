# INSTALLATION

* run `$ pip install requests pymysql` in install dependencies
* Run the SQL below to create the users table
* Setup `config.ini` with the DB details

# USAGE
Run `$ python main.py`

# LOGS
Logs are stored at `./log.log`

# SQL

```sql
CREATE TABLE IF NOT EXISTS `users` (
        `id` bigint(100) unsigned NOT NULL,
        `username` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
        `fullname` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
        `bio` text COLLATE utf8mb4_unicode_ci NOT NULL,
        `website` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
        `avatar` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
        `count_media` int(10) unsigned NOT NULL,
        `count_followers` int(10) unsigned NOT NULL,
        `count_follows` int(10) unsigned NOT NULL,
        `user_id` bigint(100) NOT NULL
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
      ALTER TABLE `users`
        ADD PRIMARY KEY (`id`);
      ALTER TABLE `users`
        MODIFY `id` bigint(100) unsigned NOT NULL AUTO_INCREMENT;
```
