USE [PRACTIC]

-- query console 1
select @@SPID
select @@TRANCOUNT
DBCC USEROPTIONS


delete from Owners

insert into Owners (OWNER_ID, name, contact) values (1, 'name1', 'email')
insert into Owners (OWNER_ID, name, contact) values (2, 'namec2', 'email')

select* from Owners

begin tran
waitfor delay '00:00:10'
insert into Owners (OWNER_ID, name, contact) values (3, 'name3', 'email3')
exec sp_log_changes null, 3, 'Phantom 1: insert'
exec sp_log_locks 'Phantom 1: after insert'
commit tran

