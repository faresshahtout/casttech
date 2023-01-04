# from .models import casts
# obj = questions.objects.get(user=request.user)
# wristwidht='wristwidht'
# wristhight='wristhight'
# clearance='clearance'
# ABsection='ABsection'
# Bwidth='Bwidth'
# Bhight='Bhight'
# castthikness='castthikness'
# BCsection='BCsection'
# Chight='Chight'
# Cwidth='Cwidth'
# circulediameter='circulediameter'
# hangangle='hangangle'
# leftpump='leftpump'
# handtip='handtip'
# rightpump='rightpump'
# midhandthikness='midhandthikness'
# palmlength='palmlength'
# palmwidth='palmwidth'
# thumby='thumby'
class scriptexec:
    def __init__(self, wristwidht=0, wristhight=0, clearance=0, ABsection=0, Bwidth=0, Bhight=0, castthikness=0,
                 BCsection=0, Chight=0, Cwidth=0, circulediameter=0, hangangle=0, leftpump=0
                 , handtip=0, rightpump=0, midhandthikness=0, palmlength=0, palmwidth=0, thumby=0,
                 patientname="johndoe",doctor="dr.johndoe"):
        with open('C:/Users/fares sh/Desktop/web/orange-madq-fe/modq_fa/Casts/designtest-1.py', "rt") as file:
            x = file.read()
        with open("file1.txt", "wt") as file:
            x = x.replace("'wristwidhtv'", str(wristwidht))
            x = x.replace("'wristhightv'", str(wristhight))
            x = x.replace("'clearancev'", str(clearance))
            x = x.replace("'ABsectionv'", str(ABsection))
            x = x.replace("'Bwidthv'", str(Bwidth))
            x = x.replace("'Bhightv'", str(Bhight))
            x = x.replace("'castthiknessv'", str(castthikness))
            x = x.replace("'BCsectionv'", str(BCsection))
            x = x.replace("'Chightv'", str(Chight))
            x = x.replace("'Cwidthv'", str(Cwidth))
            x = x.replace("'circulediameterv'", str(circulediameter))
            x = x.replace("'hanganglev'", str(hangangle))
            x = x.replace("'leftpumpv'", str(leftpump))
            x = x.replace("'handtipv'", str(handtip))
            x = x.replace("'rightpumpv'", str(rightpump))
            x = x.replace("'midhandthiknessv'", str(midhandthikness))
            x = x.replace("'palmlengthv'", str(palmlength))
            x = x.replace("'palmwidthv'", str(palmwidth))
            x = x.replace("'thumbyv'", str(thumby))
        # the v stands for value

        g = open("C:/Users/fares sh/Desktop/web/orange-madq-fe/modq_fa/Doctors-orders/%s-%s.py" % (patientname,doctor), "wt")
        g.write(x)

