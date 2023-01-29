# Dit project is een oefening om met tensorflow te werken.
## Dit project is gemaakt voor een het examenvak Innovatie.

Voor het examenvak Innovaite wilde ik mijzelf tensorflow leren. Hiervoor heb ik een aantal tutorials gevolgd.
Het eindresultaat is een programma waarmee je een model kan trainen gebaseerd op de foto's in gelabelde mappen in de trainSet map.
De labels worden automatisch uit de map namen gehaald.
Het model word opgeslagen zodat deze ergens anders gebruikt kan worden.

### foto's bewerken

Omdat de foto's aan bepaalde eisen moeten voldoen heb ik een script geschreven om de foto's te bewerken.
Schaal.py neemt de foto's uit de map input en vraagt om de naam die je wilt geven aan de foto's. Vervolgens worden de foto's bewerkt en opgeslagen als [naam]_[nummer].jpg in de map output.

### website

Er is een simpele flask webserver die gebruik maakt van het getrainde model. Er kan een afbeelding worden geupload en het model zal proberen te raden wat er op de foto staat.