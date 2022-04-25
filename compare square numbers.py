import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

array1 = [121, 144, 19, 161, 19, 144, 19, 11]
array2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

def comp(array1, array2):
    currentCheck = 1
    positionA2 = 0
    checkA2 = array2[positionA2]
    positionA1 = 0
    checkA1 = array1[positionA1]*array1[positionA1]
    logging.debug("start program")
    while currentCheck < len(array1):
        if positionA1 >= len(array1):
            return False
        checkA2 = array2[positionA2]
        checkA1 = array1[positionA1]*array1[positionA1]
        logging.debug(f"checkA2 is {checkA2}")
        logging.debug(f"checkA1 is {checkA1}")
        logging.debug(f"currentCheck is {currentCheck}")
        if checkA2 != checkA1:
            positionA1 += 1
            logging.debug(f"positionA1 is {positionA1}")
        elif checkA2 == checkA1:
            positionA2 += 1
            positionA1 = 0
            currentCheck += 1
            logging.debug(f"positionA1 is {positionA1}")
            logging.debug(f"positionA2 is {positionA2}")
    return True