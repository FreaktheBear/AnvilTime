# Pi Pico local time class including daylight saving
# Time zones https://www.worlddata.info/timezones/
# See additional readme file for changed unique zone abbreviations
# Daylight savings ref. formulas : http://www.webexhibits.org/daylightsaving/i.html

import ntptime
import time


class localtime:
    def __init__(self, land_code, daylight_saving):
        self.land_code = land_code
        self.daylight_saving = daylight_saving
    
    def get_local_time(self):        
        year = time.localtime()[0]

        # Define time differences based on land codes, see excel reference sheet in repository
        time_offsets = {
            # Americas
            'AK' : {'DT' : time.mktime((year,3,(14-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'DT_offset' : (-8*3600),
                    'ST' : time.mktime((year,11,(7-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'ST_offset' : (-9*3600)},
            'ATL' : {'DT' : time.mktime((year,3,(14-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'DT_offset' : (-3*3600),
                    'ST' : time.mktime((year,11,(7-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'ST_offset' : (-4*3600)},
            'CEN' : {'DT' : time.mktime((year,3,(14-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'DT_offset' : (-5*3600),
                    'ST' : time.mktime((year,11,(7-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'ST_offset' : (-6*3600)},
            'CL' : {'ST' : time.mktime((year,4,(7-(int(5*year/4+4))%7),3,0,0,0,0,0)), 'ST_offset' : (-4*3600),
                    'DT' : time.mktime((year,9,(30-(int(5*year/4+5))%7),2,0,0,0,0,0)), 'DT_offset' : (-3*3600)},
            'CU' : {'DT' : time.mktime((year,3,(14-(int(5*year/4+1))%7),0,0,0,0,0,0)), 'DT_offset' : (-4*3600),
                    'ST' : time.mktime((year,11,(7-(int(5*year/4+1))%7),1,0,0,0,0,0)), 'ST_offset' : (-5*3600)},
            'EAS' : {'DT' : time.mktime((year,3,(14-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'DT_offset' : (-4*3600),
                    'ST' : time.mktime((year,11,(7-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'ST_offset' : (-5*3600)},
            'AI' : {'DT' : time.mktime((year,3,(14-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'DT_offset' : (-9*3600),
                    'ST' : time.mktime((year,11,(7-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'ST_offset' : (-10*3600)},
            'MOU' : {'DT' : time.mktime((year,3,(14-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'DT_offset' : (-6*3600),
                    'ST' : time.mktime((year,11,(7-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'ST_offset' : (-7*3600)},
            'NFL' : {'DT' : time.mktime((year,3,(14-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'DT_offset' : int(-2.5*3600),
                     'ST' : time.mktime((year,11,(7-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'ST_offset' : int(-3.5*3600)},
            'PAC' : {'DT' : time.mktime((year,3,(14-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'DT_offset' : (-7*3600),
                    'ST' : time.mktime((year,11,(7-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'ST_offset' : (-8*3600)},
            'PY' : {'ST' : time.mktime((year,3,(28-(int(5*year/4+1))%7),0,0,0,0,0,0)), 'ST_offset' : (-4*3600),
                    'DT' : time.mktime((year,10,(7-(int(5*year/4+5))%7),1,0,0,0,0,0)), 'DT_offset' : (-3*3600)},
            'PM' : {'DT' : time.mktime((year,3,(14-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'DT_offset' : (-2*3600),
                    'ST' : time.mktime((year,11,(7-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'ST_offset' : (-3*3600)},
            'WG' : {'DT' : time.mktime((year,3,(31-(int(5*year/4+4))%7),0,0,0,0,0,0)), 'DT_offset' : (-1*3600),
                    'ST' : time.mktime((year,10,(31-(int(5*year/4+1))%7),1,0,0,0,0,0)), 'ST_offset' : (-2*3600)},
            # Europe
            'CE' : {'DT' : time.mktime((year,3,(31-(int(5*year/4+4))%7),1,0,0,0,0,0)), 'DT_offset' : (2*3600),
                    'ST' : time.mktime((year,10,(31-(int(5*year/4+1))%7),1,0,0,0,0,0)), 'ST_offset' : (1*3600)},
            'EE' : {'DT' : time.mktime((year,3,(31-(int(5*year/4+4))%7),3,0,0,0,0,0)), 'DT_offset' : (3*3600),
                    'ST' : time.mktime((year,10,(31-(int(5*year/4+1))%7),4,0,0,0,0,0)), 'ST_offset' : (2*3600)},
            'WE' : {'DT' : time.mktime((year,3,(31-(int(5*year/4+4))%7),1,0,0,0,0,0)), 'DT_offset' : (1*3600),
                    'ST' : time.mktime((year,10,(31-(int(5*year/4+1))%7),1,0,0,0,0,0)), 'ST_offset' : (0)},
            # Africa
            'UTC' : {'ST_offset' : (0)},
            # Asia
            'IS' : {'DT' : time.mktime((year,3,(29-(int(5*year/4+4))%7),2,0,0,0,0,0)), 'DT_offset' : (3*3600),
                    'ST' : time.mktime((year,10,(31-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'ST_offset' : (2*3600)},
            # Australia
            'AUC' : {'ST' : time.mktime((year,4,(7-(int(5*year/4+4))%7),3,0,0,0,0,0)), 'ST_offset' : int(9.5*3600),
                    'DT' : time.mktime((year,10,(7-(int(5*year/4+5))%7),2,0,0,0,0,0)), 'DT_offset' : int(10.5*3600)},

            'AUE' : {'ST' : time.mktime((year,4,(7-(int(5*year/4+4))%7),3,0,0,0,0,0)), 'ST_offset' : (10*3600),
                    'DT' : time.mktime((year,10,(7-(int(5*year/4+5))%7),2,0,0,0,0,0)), 'DT_offset' : (11*3600)},
            'LH' : {'ST' : time.mktime((year,4,(7-(int(5*year/4+4))%7),3,0,0,0,0,0)), 'ST_offset' : int(10.5*3600),
                     'DT' : time.mktime((year,10,(7-(int(5*year/4+5))%7),2,0,0,0,0,0)), 'DT_offset' : (11*3600)},
            # Indian Ocean

            # Pacific Ocean
            'CHA' : {'ST' : time.mktime((year,4,(7-(int(5*year/4+4))%7),3,0,0,0,0,0)), 'ST_offset' : int(12.75*3600),
                    'DT' : time.mktime((year,9,(30-(int(5*year/4+5))%7),2,0,0,0,0,0)), 'DT_offset' : int(13.75*3600)},
            'EAI' : {'ST' : time.mktime((year,4,(7-(int(5*year/4+5))%7),22,0,0,0,0,0)), 'ST_offset' : (-6*3600),
                    'DT' : time.mktime((year,9,(7-(int(5*year/4+4))%7),22,0,0,0,0,0)), 'DT_offset' : (-5*3600)},
            'NZ' : {'ST' : time.mktime((year,4,(7-(int(5*year/4+4))%7),3,0,0,0,0,0)), 'ST_offset' : (12*3600),
                    'DT' : time.mktime((year,9,(30-(int(5*year/4+5))%7),2,0,0,0,0,0)), 'DT_offset' : (13*3600)},

            'NF' : {'ST' : time.mktime((year,4,(7-(int(5*year/4+4))%7),3,0,0,0,0,0)), 'ST_offset' : (11*3600),
                    'DT' : time.mktime((year,9,(30-(int(5*year/4+5))%7),2,0,0,0,0,0)), 'DT_offset' : (12*3600)},
            # Atlantic Ocean
            'AZO' : {'DT' : time.mktime((year,3,(31-(int(5*year/4+4))%7),1,0,0,0,0,0)), 'DT_offset' : (0),
                    'ST' : time.mktime((year,10,(31-(int(5*year/4+1))%7),1,0,0,0,0,0)), 'ST_offset' : (-1*3600)},
            # Others
            '+14' : {'ST_offset' : (14*3600)},
            '+13' : {'ST_offset' : (13*3600)},
            '+12' : {'ST_offset' : (12*3600)},
            '+11' : {'ST_offset' : (11*3600)},
            '+10' : {'ST_offset' : (10*3600)},
            '+9' : {'ST_offset' : (9*3600)},
            '+8.75' : {'ST_offset' : int(8.75*3600)},
            '+8' : {'ST_offset' : (8*3600)},
            '+7' : {'ST_offset' : (7*3600)},
            '+6.5' : {'ST_offset' : int(6.5*3600)},
            '+6' : {'ST_offset' : (6*3600)},
            '+5.75' : {'ST_offset' : int(5.75*3600)},
            '+5.5' : {'ST_offset' : int(5.5*3600)},
            '+5' : {'ST_offset' : (5*3600)},
            '+4.5' : {'ST_offset' : int(4.5*3600)},
            '+4' : {'ST_offset' : (4*3600)},
            '+3.5' : {'ST_offset' : int(3.5*3600)},
            '+3' : {'ST_offset' : (3*3600)},
            '+2' : {'ST_offset' : (2*3600)},
            '+1' : {'ST_offset' : (1*3600)},
            '-1' : {'ST_offset' : (-1*3600)},
            '-2' : {'ST_offset' : (-2*3600)},
            '-3' : {'ST_offset' : (-3*3600)},
            '-4' : {'ST_offset' : (-4*3600)},            
            '-5' : {'ST_offset' : (-5*3600)},
            '-6' : {'ST_offset' : (-6*3600)},
            '-8' : {'ST_offset' : (-8*3600)},
            '-9' : {'ST_offset' : (-9*3600)},
            '-9.5' : {'ST_offset' : int(-9.5*3600)},
            '-10' : {'ST_offset' : (-10*3600)},
            '-11' : {'ST_offset' : (-11*3600)}

            # Add/remove countries and their offsets as needed
        }
            
        if self.daylight_saving == True and self.land_code in time_offsets:
            land_info=time_offsets[self.land_code]
            nowutc=time.time()
            nowutc_ns=time.time_ns()
            nanoseconds=(nowutc_ns%1000000000)
            f=str(int(nanoseconds/1000))                  
            if nowutc < land_info['ST']:               		                    # We are before standard time changeover
                local_time=time.localtime(nowutc+land_info['DT_offset'])
                yyyy = str(local_time[0])                                       # Create year string  
                m = local_time[1]                                               # Create month string
                if m < 10:
                    mm = "0"+str(m)
                else:
                    mm = str(m)        
                d = local_time[2]                                               # Create day string
                if d < 10:
                    dd = "0"+str(d)
                else:
                    dd = str(d)        
                H = local_time[3]                                               # Create hour string
                if H < 10:
                    HH = "0"+str(H)
                else:
                    HH = str(H)
                M = local_time[4]                                               # Create minute string
                if M < 10:
                    MM = "0"+str(M)
                else:
                    MM = str(M)
                S = local_time[5]                                               # Create second string
                if S < 10:
                    SS = "0"+str(S)
                else:
                    SS = str(S)
                local_time_str = (yyyy+"-"+mm+"-"+dd+" "+HH+":"+MM+":"+SS+"."+f) 
            elif nowutc < land_info['DT']:           		                    # we are before daylight saving time changeover
                local_time=time.localtime(nowutc+land_info['ST_offset'])
                yyyy = str(local_time[0])                                       # Create year string  
                m = local_time[1]                                               # Create month string
                if m < 10:
                    mm = "0"+str(m)
                else:
                    mm = str(m)        
                d = local_time[2]                                               # Create day string
                if d < 10:
                    dd = "0"+str(d)
                else:
                    dd = str(d)        
                H = local_time[3]                                               # Create hour string
                if H < 10:
                    HH = "0"+str(H)
                else:
                    HH = str(H)
                M = local_time[4]                                               # Create minute string
                if M < 10:
                    MM = "0"+str(M)
                else:
                    MM = str(M)
                S = local_time[5]                                               # Create second string
                if S < 10:
                    SS = "0"+str(S)
                else:
                    SS = str(S)
                local_time_str = (yyyy+"-"+mm+"-"+dd+" "+HH+":"+MM+":"+SS+"."+f)
            else:                            			                        # we are after daylight saving time changeover
                local_time=time.localtime(nowutc+land_info['DT_offset'])
                yyyy = str(local_time[0])                                       # Create year string  
                m = local_time[1]                                               # Create month string
                if m < 10:
                    mm = "0"+str(m)
                else:
                    mm = str(m)        
                d = local_time[2]                                               # Create day string
                if d < 10:
                    dd = "0"+str(d)
                else:
                    dd = str(d)        
                H = local_time[3]                                               # Create hour string
                if H < 10:
                    HH = "0"+str(H)
                else:
                    HH = str(H)
                M = local_time[4]                                               # Create minute string
                if M < 10:
                    MM = "0"+str(M)
                else:
                    MM = str(M)
                S = local_time[5]                                               # Create second string
                if S < 10:
                    SS = "0"+str(S)
                else:
                    SS = str(S)
                local_time_str = (yyyy+"-"+mm+"-"+dd+" "+HH+":"+MM+":"+SS+"."+f)            
            return(local_time, local_time_str)
        elif self.daylight_saving == False and self.land_code in time_offsets:
            land_info=time_offsets[self.land_code]
            nowutc=time.time()
            nowutc_ns=time.time_ns()
            nanoseconds=(nowutc_ns%1000000000)
            f=str(int(nanoseconds/1000)) 
            local_time=time.localtime(nowutc+land_info['ST_offset'])
            yyyy = str(local_time[0])                                       # Create year string  
            m = local_time[1]                                               # Create month string
            if m < 10:
                mm = "0"+str(m)
            else:
                mm = str(m)        
            d = local_time[2]                                               # Create day string
            if d < 10:
                dd = "0"+str(d)
            else:
                dd = str(d)        
            H = local_time[3]                                               # Create hour string
            if H < 10:
                HH = "0"+str(H)
            else:
                HH = str(H)
            M = local_time[4]                                               # Create minute string
            if M < 10:
                MM = "0"+str(M)
            else:
                MM = str(M)
            S = local_time[5]                                               # Create second string
            if S < 10:
                SS = "0"+str(S)
            else:
                SS = str(S)
            local_time_str = (yyyy+"-"+mm+"-"+dd+" "+HH+":"+MM+":"+SS+"."+f)
            return(local_time, local_time_str)
        else:return(None)

