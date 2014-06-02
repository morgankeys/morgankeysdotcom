drop table if exists users;
create table users (
  uid integer primary key autoincrement,
  username text not null,
  text text not null
);