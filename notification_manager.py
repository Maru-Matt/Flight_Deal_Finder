# This class is responsible for sending notifications with the deal flight details.
from twilio.rest import Client

account_sid = "AC04b6d768ef5c9f7b9093afe4ed0ce2cb"
auth_token = "a3d9385d3038abae2ad218eb1f125183"
phone = "+18573845253"


class NotificationManager:

    def alert(self, diparture, departure_iataCode, arrival, arrival_iataCode, price, start_D, startM, startY, endD, endM, endY):
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body=f"LOW price alert!!!. Its only $${price} to fly from {diparture} - {departure_iataCode} to {arrival} - {arrival_iataCode} from {start_D}/{startM}/{startY} - {endD}/{endM}/{endY}",
                from_=phone,
                to="+15713325482"
            )
        print(message.status)
