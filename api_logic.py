import models
from db import db
import datetime
import logging

import models.user_master

logging.basicConfig(filename='record.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')



class EatNSplit:
    def __init__(self):
        logging.info("Inside EatNSplit Class")
        self.currentDatetime = datetime.datetime.now()

    def addUser(self, name, image):
        try:
            initialBalance = 0
            # currentDatetime = datetime.datetime.now()
            userData = {
                'name':name,
                'image':image,
                'balance': initialBalance,
                'is_active':'Y',
                'created_datetime':self.currentDatetime
            }

            userMasterObject = models.UserMaster(**userData)
            db.session.add(userMasterObject)
            db.session.commit()

            message = "New user added successfully"
            return message
        except Exception as e:
            logging.error(str(e))

    def getDetails(self):
        try:
            allData = []
            allDataObject = models.UserMaster.query.all()

            for i in allDataObject:
                allData.append(i.to_dict())

            return allData
        
        except Exception as e:
            logging.error(str(e))

        
    def editBalance(self, id, newBalance):
        try:
            userObject = models.UserMaster.query.filter_by(id=id).first()

            if userObject:
                userObject.balance += newBalance

                db.session.add(userObject)
                db.session.commit()

                message = 'Balance updated for user with id: {}'.format(id)
                return message
            
            return 'User with id:{} not found'.format(id)

        except Exception as e:
            logging.error(str(e))
            

