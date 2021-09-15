# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# 
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
# 
#     https://www.apache.org/licenses/LICENSE-2.0
# 
# or in the "license" file accompanying this file. This file is distributed 
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either 
# express or implied. See the License for the specific language governing 
# permissions and limitations under the License.

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
## @type: DataSource
## @args: [database = "backuprestoredb", table_name = "rawdata", transformation_ctx = "datasource0"]
## @return: datasource0
## @inputs: []
datasource0 = glueContext.create_dynamic_frame.from_catalog(database = "backuprestoredb", table_name = "rawdata", transformation_ctx = "datasource0")
## @type: ApplyMapping
## @args: [mapping = [("coordinates.type", "string", "coordinates.type", "string"), ("coordinates.coordinates", "array", "coordinates.coordinates", "array"), ("retweeted", "boolean", "retweeted", "boolean"), ("source", "string", "source", "string"), ("entities.hashtags", "array", "entities.hashtags", "array"), ("entities.urls", "array", "entities.urls", "array"), ("reply_count", "long", "reply_count", "long"), ("favorite_count", "long", "favorite_count", "long"), ("geo.type", "string", "geo.type", "string"), ("geo.coordinates", "array", "geo.coordinates", "array"), ("id_str", "string", "id_str", "string"), ("timestamp_ms", "long", "timestamp_ms", "long"), ("truncated", "boolean", "truncated", "boolean"), ("text", "string", "text", "string"), ("retweet_count", "long", "retweet_count", "long"), ("id", "long", "id", "long"), ("possibly_sensitive", "boolean", "possibly_sensitive", "boolean"), ("filter_level", "string", "filter_level", "string"), ("created_at", "string", "created_at", "string"), ("place.id", "string", "place.id", "string"), ("place.url", "string", "place.url", "string"), ("place.place_type", "string", "place.place_type", "string"), ("place.name", "string", "place.name", "string"), ("place.full_name", "string", "place.full_name", "string"), ("place.country_code", "string", "place.country_code", "string"), ("place.country", "string", "place.country", "string"), ("place.bounding_box.type", "string", "place.bounding_box.type", "string"), ("place.bounding_box.coordinates", "array", "place.bounding_box.coordinates", "array"), ("favorited", "boolean", "favorited", "boolean"), ("lang", "string", "lang", "string"), ("in_reply_to_screen_name", "string", "in_reply_to_screen_name", "string"), ("is_quote_status", "boolean", "is_quote_status", "boolean"), ("in_reply_to_user_id_str", "string", "in_reply_to_user_id_str", "string"), ("user.id", "long", "user.id", "long"), ("user.id_str", "string", "user.id_str", "string"), ("user.name", "string", "user.name", "string"), ("user.screen_name", "string", "user.screen_name", "string"), ("user.location", "string", "user.location", "string"), ("user.url", "string", "user.url", "string"), ("user.description", "string", "user.description", "string"), ("user.translator_type", "string", "user.translator_type", "string"), ("user.protected", "boolean", "user.protected", "boolean"), ("user.verified", "boolean", "user.verified", "boolean"), ("user.followers_count", "long", "user.followers_count", "long"), ("user.friends_count", "long", "user.friends_count", "long"), ("user.listed_count", "long", "user.listed_count", "long"), ("user.favourites_count", "long", "user.favourites_count", "long"), ("user.statuses_count", "long", "user.statuses_count", "long"), ("user.created_at", "string", "user.created_at", "string"), ("user.utc_offset", "long", "user.utc_offset", "long"), ("user.time_zone", "string", "user.time_zone", "string"), ("user.geo_enabled", "boolean", "user.geo_enabled", "boolean"), ("user.lang", "string", "user.lang", "string"), ("user.contributors_enabled", "boolean", "user.contributors_enabled", "boolean"), ("user.is_translator", "boolean", "user.is_translator", "boolean"), ("user.profile_background_color", "string", "user.profile_background_color", "string"), ("user.profile_background_image_url", "string", "user.profile_background_image_url", "string"), ("user.profile_background_image_url_https", "string", "user.profile_background_image_url_https", "string"), ("user.profile_background_tile", "boolean", "user.profile_background_tile", "boolean"), ("user.profile_link_color", "string", "user.profile_link_color", "string"), ("user.profile_sidebar_border_color", "string", "user.profile_sidebar_border_color", "string"), ("user.profile_sidebar_fill_color", "string", "user.profile_sidebar_fill_color", "string"), ("user.profile_text_color", "string", "user.profile_text_color", "string"), ("user.profile_use_background_image", "boolean", "user.profile_use_background_image", "boolean"), ("user.profile_image_url", "string", "user.profile_image_url", "string"), ("user.profile_image_url_https", "string", "user.profile_image_url_https", "string"), ("user.profile_banner_url", "string", "user.profile_banner_url", "string"), ("user.default_profile", "boolean", "user.default_profile", "boolean"), ("user.default_profile_image", "boolean", "user.default_profile_image", "boolean"), ("quote_count", "long", "quote_count", "long"), ("year", "string", "year_ingested", "string"), ("month", "string", "month_ingested", "string"), ("day", "string", "day_ingested", "string")], transformation_ctx = "applymapping1"]
## @return: applymapping1
## @inputs: [frame = datasource0]
applymapping1 = ApplyMapping.apply(frame = datasource0, mappings = [("coordinates.type", "string", "coordinates.type", "string"), ("coordinates.coordinates", "array", "coordinates.coordinates", "array"), ("retweeted", "boolean", "retweeted", "boolean"), ("source", "string", "source", "string"), ("entities.hashtags", "array", "entities.hashtags", "array"), ("entities.urls", "array", "entities.urls", "array"), ("reply_count", "long", "reply_count", "long"), ("favorite_count", "long", "favorite_count", "long"), ("geo.type", "string", "geo.type", "string"), ("geo.coordinates", "array", "geo.coordinates", "array"), ("id_str", "string", "id_str", "string"), ("timestamp_ms", "long", "timestamp_ms", "long"), ("truncated", "boolean", "truncated", "boolean"), ("text", "string", "text", "string"), ("retweet_count", "long", "retweet_count", "long"), ("id", "long", "id", "long"), ("possibly_sensitive", "boolean", "possibly_sensitive", "boolean"), ("filter_level", "string", "filter_level", "string"), ("created_at", "string", "created_at", "string"), ("place.id", "string", "place.id", "string"), ("place.url", "string", "place.url", "string"), ("place.place_type", "string", "place.place_type", "string"), ("place.name", "string", "place.name", "string"), ("place.full_name", "string", "place.full_name", "string"), ("place.country_code", "string", "place.country_code", "string"), ("place.country", "string", "place.country", "string"), ("place.bounding_box.type", "string", "place.bounding_box.type", "string"), ("place.bounding_box.coordinates", "array", "place.bounding_box.coordinates", "array"), ("favorited", "boolean", "favorited", "boolean"), ("lang", "string", "lang", "string"), ("in_reply_to_screen_name", "string", "in_reply_to_screen_name", "string"), ("is_quote_status", "boolean", "is_quote_status", "boolean"), ("in_reply_to_user_id_str", "string", "in_reply_to_user_id_str", "string"), ("user.id", "long", "user.id", "long"), ("user.id_str", "string", "user.id_str", "string"), ("user.name", "string", "user.name", "string"), ("user.screen_name", "string", "user.screen_name", "string"), ("user.location", "string", "user.location", "string"), ("user.url", "string", "user.url", "string"), ("user.description", "string", "user.description", "string"), ("user.translator_type", "string", "user.translator_type", "string"), ("user.protected", "boolean", "user.protected", "boolean"), ("user.verified", "boolean", "user.verified", "boolean"), ("user.followers_count", "long", "user.followers_count", "long"), ("user.friends_count", "long", "user.friends_count", "long"), ("user.listed_count", "long", "user.listed_count", "long"), ("user.favourites_count", "long", "user.favourites_count", "long"), ("user.statuses_count", "long", "user.statuses_count", "long"), ("user.created_at", "string", "user.created_at", "string"), ("user.utc_offset", "long", "user.utc_offset", "long"), ("user.time_zone", "string", "user.time_zone", "string"), ("user.geo_enabled", "boolean", "user.geo_enabled", "boolean"), ("user.lang", "string", "user.lang", "string"), ("user.contributors_enabled", "boolean", "user.contributors_enabled", "boolean"), ("user.is_translator", "boolean", "user.is_translator", "boolean"), ("user.profile_background_color", "string", "user.profile_background_color", "string"), ("user.profile_background_image_url", "string", "user.profile_background_image_url", "string"), ("user.profile_background_image_url_https", "string", "user.profile_background_image_url_https", "string"), ("user.profile_background_tile", "boolean", "user.profile_background_tile", "boolean"), ("user.profile_link_color", "string", "user.profile_link_color", "string"), ("user.profile_sidebar_border_color", "string", "user.profile_sidebar_border_color", "string"), ("user.profile_sidebar_fill_color", "string", "user.profile_sidebar_fill_color", "string"), ("user.profile_text_color", "string", "user.profile_text_color", "string"), ("user.profile_use_background_image", "boolean", "user.profile_use_background_image", "boolean"), ("user.profile_image_url", "string", "user.profile_image_url", "string"), ("user.profile_image_url_https", "string", "user.profile_image_url_https", "string"), ("user.profile_banner_url", "string", "user.profile_banner_url", "string"), ("user.default_profile", "boolean", "user.default_profile", "boolean"), ("user.default_profile_image", "boolean", "user.default_profile_image", "boolean"), ("quote_count", "long", "quote_count", "long"), ("year", "string", "year_ingested", "string"), ("month", "string", "month_ingested", "string"), ("day", "string", "day_ingested", "string")], transformation_ctx = "applymapping1")
## @type: SelectFields
## @args: [paths = ["coordinates", "retweeted", "source", "entities", "reply_count", "favorite_count", "geo", "id_str", "timestamp_ms", "truncated", "text", "retweet_count", "id", "possibly_sensitive", "filter_level", "created_at", "place", "favorited", "lang", "in_reply_to_screen_name", "is_quote_status", "in_reply_to_user_id_str", "user", "quote_count", "year_ingested", "month_ingested", "day_ingested"], transformation_ctx = "selectfields2"]
## @return: selectfields2
## @inputs: [frame = applymapping1]
selectfields2 = SelectFields.apply(frame = applymapping1, paths = ["coordinates", "retweeted", "source", "entities", "reply_count", "favorite_count", "geo", "id_str", "timestamp_ms", "truncated", "text", "retweet_count", "id", "possibly_sensitive", "filter_level", "created_at", "place", "favorited", "lang", "in_reply_to_screen_name", "is_quote_status", "in_reply_to_user_id_str", "user", "quote_count", "year_ingested", "month_ingested", "day_ingested"], transformation_ctx = "selectfields2")
## @type: ResolveChoice
## @args: [choice = "MATCH_CATALOG", database = "backuprestoredb", table_name = "compacteddata", transformation_ctx = "resolvechoice3"]
## @return: resolvechoice3
## @inputs: [frame = selectfields2]
resolvechoice3 = ResolveChoice.apply(frame = selectfields2, choice = "MATCH_CATALOG", database = "backuprestoredb", table_name = "compacteddata", transformation_ctx = "resolvechoice3")
## @type: ResolveChoice
## @args: [choice = "make_struct", transformation_ctx = "resolvechoice4"]
## @return: resolvechoice4
## @inputs: [frame = resolvechoice3]
resolvechoice4 = ResolveChoice.apply(frame = resolvechoice3, choice = "make_struct", transformation_ctx = "resolvechoice4")
## @type: DataSink
## @args: [database = "backuprestoredb", table_name = "compacteddata", transformation_ctx = "datasink5"]
## @return: datasink5
## @inputs: [frame = resolvechoice4]
datasink5 = glueContext.write_dynamic_frame.from_catalog(frame = resolvechoice4, database = "backuprestoredb", table_name = "compacteddata", transformation_ctx = "datasink5")
job.commit()