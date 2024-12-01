--creat table question
create table question(
    question_id SERIAL,
	question_text VARCHAR(200)
);

alter table question add constraint primary_index PRIMARY KEY(question_id);
select * from question;
insert into question (question_text) values
('What is the correct way to declare a list in Python?'),
('Which of the following is used to create an immutable collection of items in Python?'),
('What will be the output of the following code?
python
Copy code
print(2 ** 3)');
  

--create table option
create table option (
    option_id SERIAL PRIMARY KEY,
	option_text VARCHAR(100),
	option_correct BOOLEAN,
	question_id INT,
	FOREIGN KEY (question_id) REFERENCES question (question_id)
);
insert into option (option_text, option_correct, question_id) values
('list = {1, 2, 3}', False, 1),
('list = [1, 2, 3]', True, 1),
('list = (1, 2, 3)', False, 1),
('list = <1, 2, 3>', False, 1),
('List', False, 2),
('Set', False, 2),
('Tuple ', True, 2),
('Dictionary', False, 2),
('5', False, 3),
('6', False, 3),
('8', True, 3),
('9', False, 3);

select * from question;
