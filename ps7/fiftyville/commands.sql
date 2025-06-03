Goal: Get broad overview of time, possible witnesses, and circumstance of abduction
SELECT * FROM crime_scene_reports;
/*Result:
id: 295
Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.
Hints: 
1. 10:15am in bakery
2. 3 witnesses
3. each witness mentions bakery
*/

Goal: Find all interview that mention bakery to get more information
SELECT * FROM interviews WHERE transcript LIKE '%bakery%';
--Result: 
/*id: 161
name: Ruth
Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.

id: 162
name: Eugene
I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma''s bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.  

id: 163
name: Raymond
As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked them person on the other end of the phone to purchase the flight ticket.

Hints:
1. Between 10:15 and 10:30, the thief got into a car in the bakery parking lot -- Check number plates of all cars that left during this time
2. Between 10:00 and 10:15, the thief withdrew money on Legett Street. -- Check account number of all withdrawals in this time
3. After 10:15,  the thief called for less than a minute. -- Check who called in this time under 1 minute
4. The thief planned to take the earliest flight out of Fiftyville. -- Check earliest flight from here
5. The other person purchased the flight ticket. --?
*/

Goal: Find names, license plates and times for those aroudn carpark around 10-11
SELECT bakery_security_logs.*, people.name FROM bakery_security_logs JOIN people ON p
eople.license_plate = bakery_security_logs.license_plate WHERE year = 2024 AND  month = 7 AND
day = 28 AND hour = 10;
/*Results:
+-----+------+-------+-----+------+--------+----------+---------------+---------+
| id  | year | month | day | hour | minute | activity | license_plate |  name   |
+-----+------+-------+-----+------+--------+----------+---------------+---------+
| 258 | 2024 | 7     | 28  | 10   | 8      | entrance | R3G7486       | Brandon |
| 259 | 2024 | 7     | 28  | 10   | 14     | entrance | 13FNH73       | Sophia  |
| 260 | 2024 | 7     | 28  | 10   | 16     | exit     | 5P2BI95       | Vanessa |
| 261 | 2024 | 7     | 28  | 10   | 18     | exit     | 94KL13X       | Bruce   |
| 262 | 2024 | 7     | 28  | 10   | 18     | exit     | 6P58WS2       | Barry   |
| 263 | 2024 | 7     | 28  | 10   | 19     | exit     | 4328GD8       | Luca    |
| 264 | 2024 | 7     | 28  | 10   | 20     | exit     | G412CB7       | Sofia   |
| 265 | 2024 | 7     | 28  | 10   | 21     | exit     | L93JTIZ       | Iman    |
| 266 | 2024 | 7     | 28  | 10   | 23     | exit     | 322W7JE       | Diana   |
| 267 | 2024 | 7     | 28  | 10   | 23     | exit     | 0NTHK55       | Kelsey  |
| 268 | 2024 | 7     | 28  | 10   | 35     | exit     | 1106N58       | Taylor  |
| 269 | 2024 | 7     | 28  | 10   | 42     | entrance | NRYN856       | Denise  |
| 270 | 2024 | 7     | 28  | 10   | 44     | entrance | WD5M8I6       | Thomas  |
| 271 | 2024 | 7     | 28  | 10   | 55     | entrance | V47T75I       | Jeremy  |
+-----+------+-------+-----+------+--------+----------+---------------+---------+

Hints:

Possible Suspects:
| 260 | 2024 | 7     | 28  | 10   | 16     | exit     | 5P2BI95       | Vanessa |
| 261 | 2024 | 7     | 28  | 10   | 18     | exit     | 94KL13X       | Bruce   |
| 262 | 2024 | 7     | 28  | 10   | 18     | exit     | 6P58WS2       | Barry   |
| 263 | 2024 | 7     | 28  | 10   | 19     | exit     | 4328GD8       | Luca    |
| 264 | 2024 | 7     | 28  | 10   | 20     | exit     | G412CB7       | Sofia   |
| 265 | 2024 | 7     | 28  | 10   | 21     | exit     | L93JTIZ       | Iman    |
| 266 | 2024 | 7     | 28  | 10   | 23     | exit     | 322W7JE       | Diana   |
| 267 | 2024 | 7     | 28  | 10   | 23     | exit     | 0NTHK55       | Kelsey  |

*/
-- Goal: Find names, times, and account number for all ATM transaction before 10:15
SELECT atm_transactions.*, people.name FROM atm_transactions
...> JOIN people ON people.id = bank_accounts.person_id
...> JOIN bank_accounts ON bank_accounts.account_number = atm_transactions.account_number
...> WHERE year = 2024 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street';

/* Result
+-----+----------------+------+-------+-----+----------------+------------------+--------+---------+
| id  | account_number | year | month | day |  atm_location  | transaction_type | amount |  name   |
+-----+----------------+------+-------+-----+----------------+------------------+--------+---------+
| 267 | 49610011       | 2024 | 7     | 28  | Leggett Street | withdraw         | 50     | Bruce   |
| 275 | 86363979       | 2024 | 7     | 28  | Leggett Street | deposit          | 10     | Kaelyn  |
| 336 | 26013199       | 2024 | 7     | 28  | Leggett Street | withdraw         | 35     | Diana   |
| 269 | 16153065       | 2024 | 7     | 28  | Leggett Street | withdraw         | 80     | Brooke  |
| 264 | 28296815       | 2024 | 7     | 28  | Leggett Street | withdraw         | 20     | Kenny   |
| 288 | 25506511       | 2024 | 7     | 28  | Leggett Street | withdraw         | 20     | Iman    |
| 246 | 28500762       | 2024 | 7     | 28  | Leggett Street | withdraw         | 48     | Luca    |
| 266 | 76054385       | 2024 | 7     | 28  | Leggett Street | withdraw         | 60     | Taylor  |
| 313 | 81061156       | 2024 | 7     | 28  | Leggett Street | withdraw         | 30     | Benista |
+-----+----------------+------+-------+-----+----------------+------------------+--------+---------+

Possible Suspects:
| 261 | 2024 | 7     | 28  | 10   | 18     | exit     | 94KL13X       | Bruce   |
| 263 | 2024 | 7     | 28  | 10   | 19     | exit     | 4328GD8       | Luca    |
| 265 | 2024 | 7     | 28  | 10   | 21     | exit     | L93JTIZ       | Iman    |
| 266 | 2024 | 7     | 28  | 10   | 23     | exit     | 322W7JE       | Diana   |
*/

-- Goal: Figure out who called for less than a minute
SELECT phone_calls.*, caller.name AS caller, receiver.name AS receiver FROM phone_cal
ls
...> JOIN people AS caller ON caller.phone_number = phone_calls.caller
...> JOIN people AS receiver ON receiver.phone_number = phone_calls.receiver
...> WHERE year = 2024 AND month = 7 AND day = 28 AND duration < 60;

/* Results: 
+-----+----------------+----------------+------+-------+-----+----------+---------+------------+
| id  |     caller     |    receiver    | year | month | day | duration | caller  |  receiver  |
+-----+----------------+----------------+------+-------+-----+----------+---------+------------+
| 221 | (130) 555-0289 | (996) 555-8899 | 2024 | 7     | 28  | 51       | Sofia   | Jack       |
| 224 | (499) 555-9472 | (892) 555-8872 | 2024 | 7     | 28  | 36       | Kelsey  | Larry      |
| 233 | (367) 555-5533 | (375) 555-8161 | 2024 | 7     | 28  | 45       | Bruce   | Robin      |
| 251 | (499) 555-9472 | (717) 555-1342 | 2024 | 7     | 28  | 50       | Kelsey  | Melissa    |
| 254 | (286) 555-6063 | (676) 555-6554 | 2024 | 7     | 28  | 43       | Taylor  | James      |
| 255 | (770) 555-1861 | (725) 555-3243 | 2024 | 7     | 28  | 49       | Diana   | Philip     |
| 261 | (031) 555-6622 | (910) 555-3251 | 2024 | 7     | 28  | 38       | Carina  | Jacqueline |
| 279 | (826) 555-1652 | (066) 555-9701 | 2024 | 7     | 28  | 55       | Kenny   | Doris      |
| 281 | (338) 555-6650 | (704) 555-2131 | 2024 | 7     | 28  | 54       | Benista | Anna       |
+-----+----------------+----------------+------+-------+-----+----------+---------+------------+

Possible Suspects:
| 261 | 2024 | 7     | 28  | 10   | 18     | exit     | 94KL13X       | Bruce   |
| 266 | 2024 | 7     | 28  | 10   | 23     | exit     | 322W7JE       | Diana   |
*/