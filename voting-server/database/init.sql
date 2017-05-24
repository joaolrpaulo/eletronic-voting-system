INSERT INTO voters(voter_id, pw_hash, name, email, city, admin) VALUES(
    11111111,
    "$pbkdf2-sha512$200000$hhAiRMh5z5lzLkXIOQfAuA$O.j4FFB0WzDYzTk1FBZ2liggPWukZ4oOxr6aQbT38uim2Q760t8wqyxywaXz4gWJIz4wQX.Awkg4w7MQPbZmFg",
    "Example User One",
    "example_user_one@gmail.com",
    "Porto",
    1
);

INSERT INTO voters(voter_id, pw_hash, name, email, city, admin) VALUES(
    22222222,
    "$pbkdf2-sha512$200000$hhAiRMh5z5lzLkXIOQfAuA$O.j4FFB0WzDYzTk1FBZ2liggPWukZ4oOxr6aQbT38uim2Q760t8wqyxywaXz4gWJIz4wQX.Awkg4w7MQPbZmFg",
    "Example User Two",
    "example_user_two@gmail.com",
    "Porto",
    1
);

INSERT INTO voters(voter_id, pw_hash, name, email, city, admin) VALUES(
    33333333,
    "$pbkdf2-sha512$200000$hhAiRMh5z5lzLkXIOQfAuA$O.j4FFB0WzDYzTk1FBZ2liggPWukZ4oOxr6aQbT38uim2Q760t8wqyxywaXz4gWJIz4wQX.Awkg4w7MQPbZmFg",
    "Example User Three",
    "example_user_three@gmail.com",
    "Porto",
    0
);

INSERT INTO voters(voter_id, pw_hash, name, email, city, admin) VALUES(
    44444444,
    "$pbkdf2-sha512$200000$hhAiRMh5z5lzLkXIOQfAuA$O.j4FFB0WzDYzTk1FBZ2liggPWukZ4oOxr6aQbT38uim2Q760t8wqyxywaXz4gWJIz4wQX.Awkg4w7MQPbZmFg",
    "Example User Four",
    "example_user_four@gmail.com",
    "Porto",
    0
);

INSERT INTO polls(title, description, image, begin_ts, end_ts, available_at) VALUES(
    "Example Votation 1",
    "Example Votation 1 Description",
    "/polls/images/1.png",
    "1483228800",
    "1491001200",
    "1483228800"
);

INSERT INTO polls_items(poll_id, title, description) VALUES(
    1,
    "Item 1",
    "Item 1 Description"
);

INSERT INTO polls_items(poll_id, title, description) VALUES(
    1,
    "Item 2",
    "Item 2 Description"
);

INSERT INTO polls_items(poll_id, title, description) VALUES(
    1,
    "Item 3",
    "Item 3 Description"
);

INSERT INTO polls_items(poll_id, title, description) VALUES(
    1,
    "Item 4",
    "Item 4 Description"
);

INSERT INTO polls(title, description, image, begin_ts, end_ts, available_at) VALUES(
    "Example Votation 2",
    "Example Votation 2 Description",
    "/polls/images/2.png",
    "1491001200",
    "1501542000",
    "1491001200"
);

INSERT INTO polls_items(poll_id, title, description) VALUES(
    2,
    "Item 1",
    "Item 1 Description"
);

INSERT INTO polls_items(poll_id, title, description) VALUES(
    2,
    "Item 2",
    "Item 2 Description"
);

INSERT INTO polls_items(poll_id, title, description) VALUES(
    2,
    "Item 3",
    "Item 3 Description"
);

INSERT INTO polls_items(poll_id, title, description) VALUES(
    2,
    "Item 4",
    "Item 4 Description"
);

INSERT INTO polls(title, description, image, begin_ts, end_ts, available_at) VALUES(
    "Example Votation 3",
    "Example Votation 3 Description",
    "/polls/images/3.png",
    "1501542000",
    "1512086400",
    "1501542000"
);

INSERT INTO polls_items(poll_id, title, description) VALUES(
    3,
    "Item 1",
    "Item 1 Description"
);

INSERT INTO polls_items(poll_id, title, description) VALUES(
    3,
    "Item 2",
    "Item 2 Description"
);

INSERT INTO polls_items(poll_id, title, description) VALUES(
    3,
    "Item 3",
    "Item 3 Description"
);

INSERT INTO polls_items(poll_id, title, description) VALUES(
    3,
    "Item 4",
    "Item 4 Description"
);

INSERT INTO polls_voters(poll_id, voter_id) VALUES(
    1,
    11111111
);

INSERT INTO polls_voters(poll_id, voter_id) VALUES(
    2,
    11111111
);

INSERT INTO polls_voters(poll_id, voter_id) VALUES(
    3,
    11111111
);

INSERT INTO polls_voters(poll_id, voter_id) VALUES(
    1,
    22222222
);

INSERT INTO polls_voters(poll_id, voter_id) VALUES(
    2,
    22222222
);

INSERT INTO polls_voters(poll_id, voter_id) VALUES(
    1,
    33333333
);

INSERT INTO polls_voters(poll_id, voter_id) VALUES(
    3,
    33333333
);

INSERT INTO polls_voters(poll_id, voter_id) VALUES(
    2,
    44444444
);
