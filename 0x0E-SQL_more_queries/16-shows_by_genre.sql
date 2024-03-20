-- Get all shows (titles) with their associated genres (names) using
-- LEFT JOINs (hbtn_0d_tvshows)
-- Ordered by show title (ascending) and then genre name (ascending).
SELECT t.`title`, g.`name`
  FROM `tv_shows` AS t
       LEFT JOIN `tv_show_genres` AS s
       ON t.`id` = s.`show_id`

       LEFT JOIN `tv_genres` AS g
       ON s.`genre_id` = g.`id`
 ORDER BY t.`title`, g.`name`;
