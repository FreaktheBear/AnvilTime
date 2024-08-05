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
            'AC' : {'ST_offset' : (-5*3600)},
            'AK' : {'DT' : time.mktime((year,3,(14-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'DT_offset' : (-8*3600),
                    'ST' : time.mktime((year,11,(7-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'ST_offset' : (-9*3600)},
            'AMZ' : {'ST_offset' : (-4*3600)},
            'AR' : {'ST_offset' : (-3*3600)},
            'ATL' : {'DT' : time.mktime((year,3,(14-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'DT_offset' : (-3*3600),
                    'ST' : time.mktime((year,11,(7-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'ST_offset' : (-4*3600)},
            'BO' : {'ST_offset' : (-4*3600)},
            'BR' : {'ST_offset' : (-3*3600)},
            'CEN' : {'DT' : time.mktime((year,3,(14-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'DT_offset' : (-5*3600),
                    'ST' : time.mktime((year,11,(7-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'ST_offset' : (-6*3600)},
            'CL' : {'ST' : time.mktime((year,4,(7-(int(5*year/4+4))%7),3,0,0,0,0,0)), 'ST_offset' : (-4*3600),
                    'DT' : time.mktime((year,9,(30-(int(5*year/4+5))%7),2,0,0,0,0,0)), 'DT_offset' : (-3*3600)},
            'CO' : {'ST_offset' : (-5*3600)},
            'CU' : {'DT' : time.mktime((year,3,(14-(int(5*year/4+1))%7),0,0,0,0,0,0)), 'DT_offset' : (-4*3600),
                    'ST' : time.mktime((year,11,(7-(int(5*year/4+1))%7),1,0,0,0,0,0)), 'ST_offset' : (-5*3600)},
            'EAS' : {'DT' : time.mktime((year,3,(14-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'DT_offset' : (-4*3600),
                    'ST' : time.mktime((year,11,(7-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'ST_offset' : (-5*3600)},
            'EC' : {'ST_offset' : (-5*3600)},
            'FN' : {'ST_offset' : (-2*3600)},
            'GF' : {'ST_offset' : (-3*3600)},
            'GY' : {'ST_offset' : (-4*3600)},
            'HI' : {'ST_offset' : (-10*3600)},
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
            'PE' : {'ST_offset' : (-5*3600)},
            'PM' : {'DT' : time.mktime((year,3,(14-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'DT_offset' : (-2*3600),
                    'ST' : time.mktime((year,11,(7-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'ST_offset' : (-3*3600)},
            'SR' : {'ST_offset' : (-3*3600)},
            'UY' : {'ST_offset' : (-3*3600)},
            'VE' : {'ST_offset' : (-4*3600)},
            'WG' : {'DT' : time.mktime((year,3,(31-(int(5*year/4+4))%7),0,0,0,0,0,0)), 'DT_offset' : (-1*3600),
                    'ST' : time.mktime((year,10,(31-(int(5*year/4+1))%7),1,0,0,0,0,0)), 'ST_offset' : (-2*3600)},
            # Europe
            'CE' : {'DT' : time.mktime((year,3,(31-(int(5*year/4+4))%7),1,0,0,0,0,0)), 'DT_offset' : (2*3600),
                    'ST' : time.mktime((year,10,(31-(int(5*year/4+1))%7),1,0,0,0,0,0)), 'ST_offset' : (1*3600)},
            'EE' : {'DT' : time.mktime((year,3,(31-(int(5*year/4+4))%7),3,0,0,0,0,0)), 'DT_offset' : (3*3600),
                    'ST' : time.mktime((year,10,(31-(int(5*year/4+1))%7),4,0,0,0,0,0)), 'ST_offset' : (2*3600)},
            'MSK' : {'ST_offset' : (3*3600)},
            'SAM' : {'ST_offset' : (4*3600)},
            'TR' : {'ST_offset' : (3*3600)},
            'WE' : {'DT' : time.mktime((year,3,(31-(int(5*year/4+4))%7),1,0,0,0,0,0)), 'DT_offset' : (1*3600),
                    'ST' : time.mktime((year,10,(31-(int(5*year/4+1))%7),1,0,0,0,0,0)), 'ST_offset' : (0)},
            # Africa
            'CA' : {'ST_offset' : (2*3600)},
            'EA' : {'ST_offset' : (3*3600)},
            'SA' : {'ST_offset' : (2*3600)},
            'UTC' : {'ST_offset' : (0)},
            'WA' : {'ST_offset' : (1*3600)},
            # Asia
            'AF' : {'ST_offset' : int(4.5*3600)},
            'ALM' : {'ST_offset' : (5*3600)},
            'ANA' : {'ST_offset' : (12*3600)},
            'AQT' : {'ST_offset' : (5*3600)},
            'AS' : {'ST_offset' : (3*3600)},
            'AM' : {'ST_offset' : (4*3600)},
            'AZ' : {'ST_offset' : (4*3600)},
            'BS' : {'ST_offset' : (6*3600)},
            'BT' : {'ST_offset' : (6*3600)},
            'BN' : {'ST_offset' : (8*3600)},
            'CI' : {'ST_offset' : (8*3600)},
            'CS' : {'ST_offset' : (8*3600)},
            'CHO' : {'ST_offset' : (8*3600)},
            'TL' : {'ST_offset' : (9*3600)},
            'EI' : {'ST_offset' : (9*3600)},
            'GE' : {'ST_offset' : (4*3600)},
            'GU' : {'ST_offset' : (4*3600)},
            'HK' : {'ST_offset' : (8*3600)},
            'HOV' : {'ST_offset' : (7*3600)},
            'IN' : {'ST_offset' : int(5.5*3600)},
            'IC' : {'ST_offset' : (7*3600)},
            'IR' : {'ST_offset' : int(3.5*3600)},
            'IRK' : {'ST_offset' : (8*3600)},
            'IS' : {'DT' : time.mktime((year,3,(29-(int(5*year/4+4))%7),2,0,0,0,0,0)), 'DT_offset' : (3*3600),
                    'ST' : time.mktime((year,10,(31-(int(5*year/4+1))%7),2,0,0,0,0,0)), 'ST_offset' : (2*3600)},
            'JP' : {'ST_offset' : (9*3600)},
            'PET' : {'ST_offset' : (12*3600)},
            'KR' : {'ST_offset' : (9*3600)},
            'KRA' : {'ST_offset' : (7*3600)},
            'KG' : {'ST_offset' : (6*3600)},
            'MY' : {'ST_offset' : (8*3600)},
            'MM' : {'ST_offset' : int(6.5*3600)},
            'NP' : {'ST_offset' : int(5.75*3600)},
            'NOV' : {'ST_offset' : (7*3600)},
            'OM' : {'ST_offset' : (6*3600)},
            'ORA' : {'ST_offset' : (5*3600)},
            'PK' : {'ST_offset' : (5*3600)},
            'PH' : {'ST_offset' : (8*3600)},
            'QYZ' : {'ST_offset' : (5*3600)},
            'SAK' : {'ST_offset' : (11*3600)},
            'SG' : {'ST_offset' : (8*3600)},
            'SRE' : {'ST_offset' : (11*3600)},
            'SL' : {'ST_offset' : int(5.5*3600)},
            'TJ' : {'ST_offset' : (5*3600)},
            'TM' : {'ST_offset' : (5*3600)},
            'ULA' : {'ST_offset' : (8*3600)},
            'UZ' : {'ST_offset' : (5*3600)},
            'VLA' : {'ST_offset' : (10*3600)},
            'WI' : {'ST_offset' : (7*3600)},
            'XJ' : {'ST_offset' : (6*3600)},
            'YAK' : {'ST_offset' : (9*3600)},
            'YEK' : {'ST_offset' : (5*3600)},
            # Australia
            'AUC' : {'ST' : time.mktime((year,4,(7-(int(5*year/4+4))%7),3,0,0,0,0,0)), 'ST_offset' : int(9.5*3600),
                    'DT' : time.mktime((year,10,(7-(int(5*year/4+5))%7),2,0,0,0,0,0)), 'DT_offset' : int(10.5*3600)},
            'ACW' : {'ST_offset' : int(8.75*3600)},
            'AUE' : {'ST' : time.mktime((year,4,(7-(int(5*year/4+4))%7),3,0,0,0,0,0)), 'ST_offset' : (10*3600),
                    'DT' : time.mktime((year,10,(7-(int(5*year/4+5))%7),2,0,0,0,0,0)), 'DT_offset' : (11*3600)},
            'AUW' : {'ST_offset' : (8*3600)},
            'LH' : {'ST' : time.mktime((year,4,(7-(int(5*year/4+4))%7),3,0,0,0,0,0)), 'ST_offset' : int(10.5*3600),
                     'DT' : time.mktime((year,10,(7-(int(5*year/4+5))%7),2,0,0,0,0,0)), 'DT_offset' : (11*3600)},
            # Indian Ocean
            'CX' : {'ST_offset' : (7*3600)},
            'CC' : {'ST_offset' : int(6.5*3600)},
            'TF' : {'ST_offset' : (5*3600)},
            'IO' : {'ST_offset' : (6*3600)},
            'MV' : {'ST_offset' : (5*3600)},
            'MU' : {'ST_offset' : (4*3600)},
            'RE' : {'ST_offset' : (4*3600)},
            'SC' : {'ST_offset' : (4*3600)},
            # Pacific Ocean
            'CH' : {'ST_offset' : (10*3600)},
            'CHA' : {'ST' : time.mktime((year,4,(7-(int(5*year/4+4))%7),3,0,0,0,0,0)), 'ST_offset' : int(12.75*3600),
                    'DT' : time.mktime((year,9,(30-(int(5*year/4+5))%7),2,0,0,0,0,0)), 'DT_offset' : int(13.75*3600)},
            'CHU' : {'ST_offset' : (10*3600)},
            'CK' : {'ST_offset' : (-10*3600)},
            'EAI' : {'ST' : time.mktime((year,4,(7-(int(5*year/4+5))%7),22,0,0,0,0,0)), 'ST_offset' : (-6*3600),
                    'DT' : time.mktime((year,9,(7-(int(5*year/4+4))%7),22,0,0,0,0,0)), 'DT_offset' : (-5*3600)},
            'FJ' : {'ST_offset' : (12*3600)},
            'GAL' : {'ST_offset' : (-6*3600)},
            'GAM' : {'ST_offset' : (-9*3600)},
            'GIL' : {'ST_offset' : (12*3600)},
            'KO' : {'ST_offset' : (11*3600)},
            'LIN' : {'ST_offset' : (14*3600)},
            'MAR' : {'ST_offset' : int(-9.5*3600)},
            'MH' : {'ST_offset' : (12*3600)},
            'NR' : {'ST_offset' : (12*3600)},
            'NC' : {'ST_offset' : (11*3600)},
            'NZ' : {'ST' : time.mktime((year,4,(7-(int(5*year/4+4))%7),3,0,0,0,0,0)), 'ST_offset' : (12*3600),
                    'DT' : time.mktime((year,9,(30-(int(5*year/4+5))%7),2,0,0,0,0,0)), 'DT_offset' : (13*3600)},
            'NU' : {'ST_offset' : (-11*3600)},
            'NF' : {'ST' : time.mktime((year,4,(7-(int(5*year/4+4))%7),3,0,0,0,0,0)), 'ST_offset' : (11*3600),
                    'DT' : time.mktime((year,9,(30-(int(5*year/4+5))%7),2,0,0,0,0,0)), 'DT_offset' : (12*3600)},
            'PW' : {'ST_offset' : (9*3600)},
            'PG' : {'ST_offset' : (10*3600)},
            'PHO' : {'ST_offset' : (13*3600)},
            'PS' : {'ST_offset' : (-8*3600)},
            'PON' : {'ST_offset' : (11*3600)},
            'SS' : {'ST_offset' : (-11*3600)},
            'SB' : {'ST_offset' : (11*3600)},
            'TAH' : {'ST_offset' : (-10*3600)},
            'TK' : {'ST_offset' : (13*3600)},
            'TO' : {'ST_offset' : (13*3600)},
            'TV' : {'ST_offset' : (12*3600)},
            'VU' : {'ST_offset' : (11*3600)},
            'WAK' : {'ST_offset' : (12*3600)},
            'WF' : {'ST_offset' : (12*3600)},
            'WS' : {'ST_offset' : (13*3600)},
            # Atlantic Ocean
            'AZO' : {'DT' : time.mktime((year,3,(31-(int(5*year/4+4))%7),1,0,0,0,0,0)), 'DT_offset' : (0),
                    'ST' : time.mktime((year,10,(31-(int(5*year/4+1))%7),1,0,0,0,0,0)), 'ST_offset' : (-1*3600)},
            'CV' : {'ST_offset' : (-1*3600)},
            'FK' : {'ST_offset' : (-3*3600)},
            'GS' : {'ST_offset' : (-2*3600)},
            # Antartica
            'CAS' : {'ST_offset' : (8*3600)},
            'DAV' : {'ST_offset' : (7*3600)},
            'DDU' : {'ST_offset' : (10*3600)},
            'MAW' : {'ST_offset' : (5*3600)},
            'SYO' : {'ST_offset' : (3*3600)},
            'VOS' : {'ST_offset' : (6*3600)}
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

