def prepare_schema(data, fields, exclude):
    if fields is not None:
        allowed = set(fields)
        existing = set(data)

        for field_name in existing - allowed:
            data.pop(field_name)

    if exclude is not None:
        not_allowed = set(exclude)

        for field_name in not_allowed:
            data.pop(field_name, None)

    return data


class VenueSchemas:
    def __main_schema(self, fields=None, exclude=None):
        schema = {
            "id": 27,
            "profile_type": "venue",
            "can_be_removed": "",
            "is_request_user": '',
            "first_name": "first name",
            "last_name": "",
            "likes_count": 0,
            "liked_by_current_user": 'true',
            "email": "venue@gmail.com",
            "username": "username3",
            "photo": 'null',
            "city": {
                "id": 5199,
                "name": "Aalborg (Denmark)",
                "city_name": "Aalborg",
                "country": {
                    "id": 311,
                    "name": "Denmark",
                    "code2": "DK"
                }
            },
            "websites": 'null',
            "about": 'null',
            "last_update": "17.08.2020",
            "availability": [
                {
                    "id": 2,
                    "start": "2020-10-20",
                    "end": "2020-11-20"
                }
            ],
            "event_types": [
                {
                    "id": 3,
                    "name": "Anniversary"
                }
            ],
            "images": [
                {
                    "id": 1,
                    "url": "http://testserver/media/imagemodel/test_image3.jpeg"
                },
                {
                    "id": 2,
                    "url": "http://testserver/media/imagemodel/test_image3_Up7gu4o.jpeg"
                }
            ],
            "videos": [],
            "video_links": [
                "https://www.youtube.com/watch?v=DqjaGKQvB1Q",
                "https://www.youtube.com/watch?v=DqjaGKQvB1Q"
            ],
            "events_dates": [
                {
                    "id": 2,
                    "start": "2020-10-20",
                    "end": "2020-11-20",
                    "name": "event name"
                }
            ],
            "price": 45000,
            "has_sound_technician": 'true',
            "has_merchandising": 'false',
            "has_bar": 'false',
            "seats": 20000,
            "wattage": 1000,
            "stats_and_badges": {
                "completed_events_count": 0,
                "badge": "bronze",
                "participated_events_count": 0
            },
            "square": {
                "id": 6,
                "name": "arena 1000+m2 (for big events)",
                "people_amount": 1500
            }
        }
        return prepare_schema(schema, fields, exclude)


class PostViewSchemas:
    def __main_schema(self, fields=None, exclude=None):
        schema = {
            "id": 1,
            "title": "test title",
            "content": "content",
            "image": "http://testserver/media/postmodel/No-photo-m_dNy1ogD.png",
            "created_at": "2020-11-08T23:53:28.632526Z",
            "updated_at": "2020-11-08T23:53:28.634251Z",
            "author": {
                "id": 1,
                "first_name": "",
                "last_name": "",
                "email": "example@gmail.com",
                "photo": "http://testserver/media/usermodel/No-photo-m_2vGUsgd.png",
                "full_name": "example@gmail.com"
            },
            "comment_form": "form",
            "comments": [
                {
                    "id": 3,
                    "author": {
                        "first_name": "",
                        "last_name": "",
                        "email": "visitor@gmail.com",
                        "photo": "http://testserver/media/visitormodel/No-photo-m_2zW911s.png",
                        "full_name": "visitor@gmail.com"
                    },
                    "created_at": "09.11.2020 03:45",
                    "updated_at": "09.11.2020 03:45",
                    "text": "weather"
                }
            ]
        }

        return prepare_schema(schema, fields, exclude)

    def get_post_api_create_schema(self):
        return PostViewSchemas().__main_schema(exclude=('comments', "comment_form"))

    def get_post_detail_schema(self):
        return PostViewSchemas().__main_schema()

    def get_post_list_schema(self):
        return {
            "next_page_number": 2,
            "previous_page_number": "null",
            "has_previous": "false",
            "has_next": "true",
            "number": 1,
            "total_pages": 2,
            "results": [
                {
                    "id": 8,
                    "author": "example@gmail.com",
                    "title": "Vacancies",
                    "content": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus aliquam",
                    "image": "http://testserver/media/postmodel/No-photo-m_viJDgRH.png",
                    "created_at": "09.11.2020 00:09",
                    "updated_at": "09.11.2020 00:09"
                }
            ]
        }
