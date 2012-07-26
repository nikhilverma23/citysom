ALTER TABLE "event_eventgenre" ADD COLUMN "category_id" integer REFERENCES "event_category" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX event_eventgenre_category_id ON event_eventgenre USING btree (category_id);
 
