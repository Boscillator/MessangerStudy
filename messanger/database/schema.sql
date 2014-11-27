drop table if exists conversations;

create table conversations (
    id integer primary key autoincrement,
    user1 text not null,
    user2 text not null,
    log text not null
);