import paho.mqtt.client as mqttClient
import time
import json
#import MySQLdb
import pymysql
pymysql.install_as_MySQLdb()

HOST = "localhost"
USER_database = "root"
PASSWD = ""
DATABASE = "poultry"

def on_connect(client, userdata, flags, rc):
    if rc == 0:

        print("Connected to broker")

        global Connected  # Use global variable
        Connected = True  # Signal connection

    else:

        print("Connection failed")


def on_message(client, userdata, message):
    print ("Topic: " + message.topic +"message: " +str(message.payload))
    db = pymysql.connect(host=HOST, user=USER_database, passwd=PASSWD, db=DATABASE, charset="utf8")
    cursor = db.cursor()
    if (message.topic == "turkey/adc"):
        adc = json.loads(message.payload)
        adc = str(adc['ADC_Val'])

        insert_query = "INSERT INTO data (ADC) VALUES (%s)"
        cursor.execute(insert_query,(adc,))
        db.commit()
        # cursor.execute("SELECT Start_date FROM data WHERE Id = 1")
        # row = cursor.fetchall()
        #db.commit()

        while row is not None:
            print(row)
            row = cursor.fetchone()


    if (message.topic == "turkey/data"):
        data_message = message.payload
        data = json.loads(data_message.decode('utf-8'))
        temperature = str(data['Temp'])
        Humidity = str(data['Hum'])
        Carbon_di_oxide = str(data['Co2'])
        Amonia = str(data['NH3'])
        print(temperature)


        last_row_id = cursor.execute("SELECT Id FROM data")
        print(last_row_id)
        cursor.execute("UPDATE data SET Temperature=%s, Humidity=%s, Carbon_dy_oxide=%s, Amonia=%s WHERE Id='%s' " % (temperature, Humidity, Carbon_di_oxide, Amonia, last_row_id))
        db.commit()

    if (message.topic == "turkey/CurrentDateTime"):
        CurrentDateTime = json.loads(message.payload.decode('utf-8'))

        year = str(CurrentDateTime['y'])
        month = int(CurrentDateTime['m'])
        if(month<10):
            month = str("0" + str(month))
        else:
            month = str(month)
        Day = int(CurrentDateTime['d'])
        if (Day < 10):
            Day = str("0" + str(Day))
        else:
            Day = str(Day)
        hour = int(CurrentDateTime['H'])
        if (hour < 10):
            hour = str("0" + str(hour))
        else:
            hour = str(hour)
        minute = int(CurrentDateTime['M'])
        if (minute < 10):
            minute = str("0" + str(minute))
        else:
            minute = str(minute)
        second = int(CurrentDateTime['S'])
        if (second < 10):
            second = str("0" + str(second))
        else:
            second = str(second)

        Current_date = str(year+month+Day)
        Current_time = str(hour+minute+second)

        print(Current_date+" "+Current_time)

        last_row_id = cursor.execute("SELECT Id FROM data")

        print(last_row_id)

        cursor.execute("UPDATE data SET Cur_Date=%s, Cur_time=%s WHERE Id='%s' " % (Current_date, Current_time, last_row_id))
        db.commit()

    if (message.topic == "turkey/BatchStartDate"):
        BatchStartDate = json.loads(message.payload)

        year = str(BatchStartDate['SY'])
        month = int(BatchStartDate['SM'])
        if (month < 10):
            month = str("0" + str(month))
        else:
            month = str(month)
        Day = int(BatchStartDate['SD'])
        if (Day < 10):
            Day = str("0" + str(Day))
        else:
            Day = str(Day)

        Start_date = str(year + month + Day)

        print(Start_date)
        last_row_id = cursor.execute("SELECT Id FROM data")
        print(last_row_id)
        cursor.execute("UPDATE data SET Start_date=%s WHERE Id='%s' " % (Start_date, last_row_id))
        db.commit()

    if (message.topic == "turkey/RestartStatus"):
        RestartStatus = json.loads(message.payload)

        RestartNo = int(RestartStatus['ReStartNo'])

        hour = int(RestartStatus['H'])
        if (hour < 10):
            hour = str("0" + str(hour))
        else:
            hour = str(hour)
        minute = int(RestartStatus['M'])
        if (minute < 10):
            minute = str("0" + str(minute))
        else:
            minute = str(minute)
        second = int(RestartStatus['S'])
        if (second < 10):
            second = str("0" + str(second))
        else:
            second = str(second)

        RestartTime = str(hour+minute+second)

        print(RestartTime)
        last_row_id = cursor.execute("SELECT Id FROM data")
        print(last_row_id)
        cursor.execute("UPDATE data SET Restart_no=%s, Restart_time=%s WHERE Id='%s' " % (RestartNo, RestartTime, last_row_id))
        db.commit()

    if (message.topic == "turkey/ElapsedTime"):
        ElapsedTime = json.loads(message.payload)
        ElapsedTime=int(ElapsedTime['ElapsedTime'])


        last_row_id = cursor.execute("SELECT Id FROM data")
        print(last_row_id)
        cursor.execute("UPDATE data SET Day=%s WHERE Id='%s' " % (ElapsedTime, last_row_id))
        db.commit()


    if (message.topic == "turkey/FanStatus"):
        FanStatus = json.loads(message.payload)
        FanStatus = str(FanStatus['FanStatus'])

        last_row_id = cursor.execute("SELECT Id FROM data")
        print(last_row_id)
        cursor.execute("UPDATE data SET Fan_status=%s WHERE Id='%s' " % (FanStatus, last_row_id))
        db.commit()


    if (message.topic == "turkey/LightStatus"):
        LightStatus = json.loads(message.payload)
        LightStatus = str(LightStatus['LightStatus'])

        last_row_id = cursor.execute("SELECT Id FROM data")
        print(last_row_id)
        cursor.execute("UPDATE data SET Light_status=%s WHERE Id='%s' " % (LightStatus, last_row_id))
        db.commit()
        cursor.close()
        db.close()




Connected = False  # global variable for the state of the connection

broker_address = "182.163.112.207"  # Broker address
port = 1883  # Broker port
user = ""  # Connection username
password = ""  # Connection password

client = mqttClient.Client("Python")  # create new instance
client.username_pw_set(user, password=password)  # set username and password
client.on_connect = on_connect  # attach function to callback
client.on_message = on_message  # attach function to callback

client.connect(broker_address, port=port)  # connect to broker

client.loop_start()  # start the loop

while Connected != True:  # Wait for connection
    time.sleep(0.1)

client.subscribe("turkey/allInfo")
client.subscribe("turkey/data")
client.subscribe("turkey/ElapsedTime")
client.subscribe("turkey/adc")
client.subscribe("turkey/LightStatus")
client.subscribe("turkey/FanStatus")
client.subscribe("turkey/CurrentDateTime")
client.subscribe("turkey/BatchStartDate")
client.subscribe("turkey/RestartStatus")


try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print
    "exiting"
    client.disconnect()
    client.loop_stop()
