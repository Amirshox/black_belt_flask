classDiagram
direction BT
class bought_points_by_user_identifier {
   int user_id
   int point_id
}
class point {
   varchar(100) title
   text description
   float price
   int quantity
   int author_id
   int sold_count
   int id
}
class user {
   varchar(63) first_name
   varchar(63) last_name
   varchar(63) email
   varchar(200) password
   int id
}

point  -->  bought_points_by_user_identifier : point_id:id
user  -->  bought_points_by_user_identifier : user_id:id
user  -->  point : author_id:id
