from connection import Connection
import  drivers.brand_model as driver

class SyringePumpConnection(Connection):

    def __init__(self, name:str = "", address:str = "", socketio = None, isvirtual: bool=False, brand_model: str = None):
        super().__init__(
            name=name,
            address=address,
            socketio=socketio,
            isvirtual=isvirtual
        )

        self._driver = None

        if brand_model is None:
            raise Exception("User need to provied brand/model information for this to work correctly")
        # TODO - Based on the brand-model pick the right driver file and 
        if brand_model == "Whatever your brand/model identifier is":
            self._driver = driver #This would be the driver stored in the "./drivers/<your-brand-model>/__init__.py"
        elif brand_model == "Some ther brand/model - left for folks to expand on":
            # self._driver = blah
            raise Exception("No implementation for driver found for brand/model")
        else:
            raise Exception("No driver found for brand/model")


    # TODO - Add all the high level commands here and then call the driver, I just gave placholder
    # names here to help figure out what needs to be done, change them to your API

    def command1(self, arg1, arg2):
        data = self._driver.command1(arg1, arg2)
        self.send_data(data)
    

    def command2(self, arg1, arg2):
        data = self._driver.command1(arg1, arg2)
        self.send_data(data)


    def command3(self, arg1, arg2):
        data = self._driver.command1(arg1, arg2)
        self.send_data(data)

    def command4(self, arg1, arg2):
        data = self._driver.command1(arg1, arg2)
        self.send_data(data)


    def command5(self, arg1, arg2):
        data = self._driver.command1(arg1, arg2)
        self.send_data(data)
