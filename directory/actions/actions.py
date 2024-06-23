# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
# import arrow
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

city_db = {
    'brussels': 'Europe/Brussels',
    'zagreb': 'Europe/Zagreb',
    'london': 'Europe/Dublin',
    'lisbon': 'Europe/Lisbon',
    'amsterdam': 'Europe/Amsterdam',
    'seattle': 'US/Pacific'
}


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World!")

        return []


class ActionTellTime(Action):
    def name(self) -> Text:
        return "action_tell_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        current_place = next(tracker.get_latest_entity_values("place"), None)
        # utc = arrow.utcnow()
        # if not current_place:
        #     msg = f"It's {utc.format('HH:mm')} utc now. You can also give me a place."
        #     dispatcher.utter_message(text=msg)
        #     return []
        # tz_string = city_db.get(current_place, None)
        # if not tz_string:
        #     msg = f"It's I didn't recognize {current_place}. It is spelled correctly?"
        #     dispatcher.utter_message(text=msg)
        #     return []
        # msg = f"It's {utc.to(city_db[current_place]).format('HH:mm')} in {current_place} now."
        # dispatcher.utter_message(text=msg)
        # return []
        msg = f"It's 16:56 utc now. You can also give me a place."
        dispatcher.utter_message(text=msg)
