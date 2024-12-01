USE [PRACTIC]

-- query console 2
select @@SPID
select @@TRANCOUNT
DBCC USEROPTIONS


delete from Owners

insert into Owners (OWNER_ID, name, contact) values (1, 'name1', 'email')
insert into Owners (OWNER_ID, name, contact) values (2, 'namec2', 'email')

select* from Owners

 set transaction isolation level repeatable read
--set transaction isolation level serializable --solution
begin tran
select * from Owners
exec sp_log_locks 'Phantom 2: between selects'
waitfor delay '00:00:10'
select * from Owners
exec sp_log_locks 'Phantom 2: after both selects'
commit tran 