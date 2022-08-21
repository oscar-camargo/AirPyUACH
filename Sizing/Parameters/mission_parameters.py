
class ground():    
    @staticmethod
    def _getmethod(key=0):
        methods = [method for method in dir(ground)[28:]]
        return getattr(ground,methods[key])()
    @staticmethod
    def _conditions():
        return [getattr(ground,method)()['Condition'] for method in dir(ground)[28:]]
    @staticmethod
    def ground():
        return {'Altitude': 0, 'True Course': 0, 'Ground Incline': 0, 'Friction Coefficient': 0, 'Throttle': 0,'Initial velocity': 0,'Final velocity': 0,'Condition': 'Ground'}
    @staticmethod
    def landing():
        return {'Altitude': 0, 'True Course': 0, 'Friction Coefficient': 0, 'Throttle': 0,'Initial velocity': 0,'Final velocity': 0,'Condition': 'Landing'}
    @staticmethod
    def takeoff():
        return {'Altitude': 0, 'True Course': 0, 'Friction Coefficient': 0, 'Throttle': 0,'Initial velocity': 0,'Final velocity': 0,'Condition': 'Takeoff'}


class climb():
    @staticmethod
    def _getmethod(key=0):
        methods = [method for method in dir(climb)[28:]]
        return getattr(climb,methods[key])()
    @staticmethod
    def _conditions():
        return [getattr(climb,method)()['Condition'] for method in dir(climb)[28:]]
    @staticmethod
    def constant_CAS_constant_rate():
        return {'Starting Altitude': 0, 'Final Altitude': 0, 'True Course': 0,'Climb Rate': 0, 'CAS': 0,'Condition': 'Constant CAS Constant Rate'}
    @staticmethod
    def constant_EAS_constant_rate():
        return {'Starting Altitude': 0, 'Final Altitude': 0, 'True Course': 0,'Climb Rate': 0, 'EAS': 0,'Condition': 'Constant EAS Constant Rate'}
    @staticmethod
    def constant_M_constant_angle():
        return {'Starting Altitude': 0, 'Final Altitude': 0, 'True Course': 0,'Climb Angle': 0, 'Mach': 0,'Condition': 'Constant M Constant Angle'}
    @staticmethod
    def constant_M_constant_rate():
        return {'Starting Altitude': 0, 'Final Altitude': 0, 'True Course': 0,'Climb Rate': 0, 'Mach': 0,'Condition': 'Constant M Constant Rate'}
    @staticmethod
    def constant_M_linear_altitude():
        return {'Starting Altitude': 0, 'Final Altitude': 0, 'True Course': 0,'Distance': 0, 'Mach': 0,'Condition': 'Constant M Linear altitude'}
    @staticmethod
    def constant_Speed_constant_angle():
        return {'Starting Altitude': 0, 'Final Altitude': 0, 'True Course': 0,'Climb Angle': 0, 'Speed': 0,'Condition': 'Constant Speed Constant Angle'}
    @staticmethod
    def constant_Speed_constant_rate():
        return {'Starting Altitude': 0, 'Final Altitude': 0, 'True Course': 0,'Climb Rate': 0, 'Speed': 0,'Condition': 'Constant Speed Constant Rate'}
    @staticmethod
    def constant_Speed_linear_altitude():
        return {'Starting Altitude': 0, 'Final Altitude': 0, 'True Course': 0,'Distance': 0, 'Speed': 0,'Condition': 'Constant Speed Linear Altitude'}
    @staticmethod
    def constant_Throttle_constant_speed():
        return {'Starting Altitude': 0, 'Final Altitude': 0, 'True Course': 0,'Throttle': 0, 'Speed': 0,'Condition': 'Constant Throttle Constant Speed'}
    @staticmethod
    def constant_q_constant_angle():
        return {'Starting Altitude': 0, 'Final Altitude': 0, 'True Course': 0,'Climb Angle': 0, 'q': 0,'Condition': 'Constant q Constant Angle'}
    @staticmethod
    def constant_q_constant_rate():
        return {'Starting Altitude': 0, 'Final Altitude': 0, 'True Course': 0,'Climb Rate': 0, 'q': 0,'Condition': 'Constant q Constant Rate'}
    @staticmethod
    def linear_mach_constant_rate():
        return {'Starting Altitude': 0, 'Final Altitude': 0, 'True Course': 0, 'Climb Rate': 0, 'Initial Mach': 0, 'Final Mach': 0,'Condition': 'Linear M Constant Rate'}
    @staticmethod
    def linear_speed_constant_rate():
        return {'Starting Altitude': 0, 'Final Altitude': 0, 'True Course': 0, 'Climb Rate': 0, 'Initial Speed': 0, 'Final Speed': 0,'Condition': 'Linear Speed Constant Rate'}


class cruise():
    @staticmethod
    def _getmethod(key=0):
        methods = [method for method in dir(cruise)[28:]]
        return getattr(cruise,methods[key])()
    @staticmethod
    def _conditions():
        return [getattr(cruise,method)()['Condition'] for method in dir(cruise)[28:]]
    @staticmethod
    def constant_Acc_constant_alt():
        return {'Altitude': 0, 'True Course': 0, 'Acceleration': 0, 'Initial Speed': 0, 'Final Speed': 0,'Condition': 'Constant Acc. Constant Alt.'}
    @staticmethod
    def constant_q_constant_alt_loiter():
        return {'Altitude': 0, 'True Course': 0, 'q': 0,'Time': 0,'Condition': 'Constant q Constant Alt. Loiter'}
    @staticmethod
    def constant_q_constant_alt():
        return {'Altitude': 0, 'True Course': 0, 'q': 0,'Distance': 0,'Condition': 'Constant q Constant Alt.'}
    @staticmethod
    def constant_Mach_constant_alt_loiter():
        return {'Altitude': 0, 'True Course': 0, 'Mach': 0, 'Time': 0,'Condition': 'Constant M Constant Alt. Loiter'}
    @staticmethod
    def constant_Mach_constant_alt():
        return {'Altitude': 0, 'True Course': 0, 'Mach': 0, 'Distance': 0,'Condition': 'Constant M Constant Alt.'}
    @staticmethod
    def constant_Pitch_rate_constant_alt():
        return {'True Course': 0, 'Initial Pitch': 0, 'Final Pitch': 0, 'Pitch Rate': 0,'Condition': 'Constant Pitch rate Constant Alt.','Altitude': 0}
    @staticmethod
    def constant_Speed_constant_alt_loiter():
        return {'Altitude': 0, 'True Course': 0, 'Speed': 0, 'Time': 0,'Condition': 'Constant Speed Constant Alt. Loiter'}
    @staticmethod
    def constant_Speed_constant_alt():
        return {'Altitude': 0, 'True Course': 0, 'Speed': 0, 'Distance': 0,'Condition': 'Constant Speed Constant Alt.'}
    @staticmethod
    def constant_Throttle_constant_alt():
        return {'Altitude': 0, 'True Course': 0,'Speed': 0,'Throttle':0,'Condition': 'Constant Throttle Constant Alt.'}


class descent():
    @staticmethod
    def _getmethod(key=0):
        methods = [method for method in dir(descent)[28:]]
        return getattr(descent,methods[key])()
    @staticmethod
    def _conditions():
        return [getattr(descent,method)()['Condition'] for method in dir(descent)[28:]]
    @staticmethod
    def constant_cas_constant_rate():
        return {'Initial Altitude': 0, 'Final Altitude': 0,'True Course': 0,'Descent Rate': 0,'CAS': 0,'Condition': 'Constant CAS Constant Rate'}
    @staticmethod
    def constant_eas_constant_rate():
        return {'Initial Altitude': 0, 'Final Altitude': 0, 'True Course': 0,'Descent Rate': 0,'EAS': 0,'Condition': 'Constant EAS Constant Rate'}
    @staticmethod
    def constant_speed_constant_angle():
        return {'Initial Altitude': 0,'Final Altitude': 0,'Descent Angle': 0,'Speed': 0,'Condition': 'Constant Speed Constant Angle'}
    @staticmethod
    def constant_speed_constant_rate():
        return {'Initial Altitude': 0, 'Final Altitude': 0,'Descent Rate':0,'Speed':0,'Condition': 'Constant Speed Constant Rate'}
    @staticmethod
    def linear_mach_constant_rate():
        return {'Initial Altitude':0, 'Final Altitude': 0,'Descent Rate': 0,'Initial Mach': 0, 'Final Mach':0,'Condition': 'Linear Mach Constant Rate'}

class hover():
    @staticmethod
    def _getmethod(key=0):
        methods = [method for method in dir(hover)[28:]]
        return getattr(hover,methods[key])()
    @staticmethod
    def climb():
        return {'Initial Altitude': 0, 'Final Altitude': 0, 'True Course': 0,'Climb Rate': 0,'Condition': 'Climb'}

    @staticmethod
    def descent():
        return {'Initial Altitude': 0, 'Final Altitude': 0, 'True Course': 0,'Descent Rate': 0,'Condition': 'Descent'}

    @staticmethod
    def hover():
        return {'Altitude': 0,'True Course': 0, 'Time': 0,'Condition': 'Hover'}

    @staticmethod
    def _conditions():
        return [getattr(hover,method)()['Condition'] for method in dir(hover)[28:]]

class single_point():
    @staticmethod
    def _getmethod(key=0):
        methods = [method for method in dir(single_point)[28:]]
        return getattr(single_point,methods[key])()
    @staticmethod
    def _conditions():
        return [getattr(single_point,method)()['Condition'] for method in dir(single_point)[28:]]
    @staticmethod
    def set_speed_set_alt_noprop():
        return {'Altitude': 0, 'Speed': 0, 'Distance': 0,'Z Acceleration': 0, 'Control Points': 0,'Condition': 'Set Speed Set Alt. NoProp'}
    @staticmethod
    def set_speed_set_alt():
        return {'Altitude': 0, 'Speed': 0, 'Distance': 0, 'X Acceleration': 0, 'Z Acceleration': 0, 'Control Points': 0,'Condition': 'Set Speed Set Alt.'}
    @staticmethod
    def set_speed_set_throttle():
        return {'Altitude': 0, 'Speed': 0,'Throttle': 0,'Z Acceleration': 0, 'Control Points': 0,'Condition': 'Set Speed Set Throttle'} 

class transition():
    @staticmethod
    def _getmethod(key=0):
        methods = [method for method in dir(transition)[28:]]
        return getattr(transition,methods[key])()
    @staticmethod
    def _conditions():
        return [getattr(transition,method)()['Condition'] for method in dir(transition)[28:]]
    @staticmethod
    def constant_acc_constant_angle_linear_climb():
        a = {'Initial Altitude': 0, 'Final Altitude': 0, 'True Course': 0, 'Speed': 0, 'Climb Angle': 0, 'Acceleration': 0, 'Initial Pitch': 0, 'Final Pitch': 0,'Condition': 'C. Acc. C. Angle Linear Climb'}
        return a
    @staticmethod
    def constant_acc_constant_pitch_rate_constant_alt():
        return {'Altitude': 0, 'True Course': 0, 'Initial Speed': 0,'Final Speed': 0, 'Acceleration': 0, 'Initial Pitch': 0, 'Final Pitch': 0,'Condition': 'C. Acc. C. Pitch Rate C. Alt.'}
