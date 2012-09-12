ALTER TABLE "event_event" ADD COLUMN  "start_hours_on_monday" time;
ALTER TABLE "event_event" ADD COLUMN  "end_hours_on_monday" time;
ALTER TABLE "event_event" ADD COLUMN  "start_hours_on_tuesday" time;
ALTER TABLE "event_event" ADD COLUMN  "end_hours_on_tuesday" time;
ALTER TABLE "event_event" ADD COLUMN  "start_hours_on_wednesday" time;
ALTER TABLE "event_event" ADD COLUMN  "end_hours_on_wednesday" time;
ALTER TABLE "event_event" ADD COLUMN  "start_hours_on_thursday" time;
ALTER TABLE "event_event" ADD COLUMN  "end_hours_on_thursday" time;
ALTER TABLE "event_event" ADD COLUMN  "start_hours_on_friday" time;
ALTER TABLE "event_event" ADD COLUMN  "end_hours_on_friday" time;
ALTER TABLE "event_event" ADD COLUMN  "start_hours_on_saturday" time;
ALTER TABLE "event_event" ADD COLUMN  "end_hours_on_saturday" time;
ALTER TABLE "event_event" ADD COLUMN  "start_hours_on_sunday" time;
ALTER TABLE "event_event" ADD COLUMN  "end_hours_on_sunday" time;

ALTER TABLE "event_event" ADD COLUMN "event_start_date" date;
ALTER TABLE "event_event" ADD COLUMN "event_completion_date" date;
ALTER TABLE "event_event" ADD COLUMN "frequency" character varying(80);
ALTER TABLE "event_event" ADD COLUMN "interval" integer;
ALTER TABLE "event_event" ADD COLUMN "by_monthday" varchar(80);
ALTER TABLE "event_event" ADD COLUMN "by_month" varchar(80);

CREATE TABLE "event_event_by_day" (
    "id" serial NOT NULL PRIMARY KEY,
    "event_id" integer NOT NULL,
    "days_id" integer NOT NULL REFERENCES "event_days" ("id") DEFERRABLE INITIALLY DEFERRED,
    UNIQUE ("event_id", "days_id")
)
;

ALTER TABLE "event_performancedetails" DROP COLUMN "frequency";
ALTER TABLE "event_performancedetails" DROP COLUMN "interval";
ALTER TABLE "event_performancedetails" DROP COLUMN "by_monthday";
ALTER TABLE "event_performancedetails" DROP COLUMN "by_month";
ALTER TABLE "event_performancedetails" DROP COLUMN "date_started";
ALTER TABLE "event_performancedetails" DROP COLUMN "date_completed";
DROP TABLE "event_performancedetails_by_day";
ALTER TABLE "event_performancedetails" ADD COLUMN "date_of_performance" date;