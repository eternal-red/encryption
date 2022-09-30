import enc
from decimal import *
getcontext().prec=50
def arccos_cordic (t,n):
#    Input, real T, the cosine of an angle.  -1 <= T <= 1.
#    Input, integer N, the number of iterations to take.
#    A value of 10 is low.  Good accuracy is achieved with 20 or more
#    iterations.
  import numpy as np
  t=Decimal(t)
  angles = np.array ( [  \
    Decimal(7.8539816339744830962E-01), \
    Decimal(4.6364760900080611621E-01), \
    Decimal(2.4497866312686415417E-01), \
    Decimal(1.2435499454676143503E-01), \
    Decimal(6.2418809995957348474E-02), \
    Decimal(3.1239833430268276254E-02), \
    Decimal(1.5623728620476830803E-02), \
    Decimal(7.8123410601011112965E-03), \
    Decimal(3.9062301319669718276E-03), \
    Decimal(1.9531225164788186851E-03), \
    Decimal(9.7656218955931943040E-04), \
    Decimal(4.8828121119489827547E-04), \
    Decimal(2.4414062014936176402E-04), \
    Decimal(1.2207031189367020424E-04), \
    Decimal(6.1035156174208775022E-05), \
    Decimal(3.0517578115526096862E-05), \
    Decimal(1.5258789061315762107E-05), \
    Decimal(7.6293945311019702634E-06), \
    Decimal(3.8146972656064962829E-06), \
    Decimal(1.9073486328101870354E-06), \
    Decimal(9.5367431640596087942E-07), \
    Decimal(4.7683715820308885993E-07), \
    Decimal(2.3841857910155798249E-07), \
    Decimal(1.1920928955078068531E-07), \
    Decimal(5.9604644775390554414E-08), \
    Decimal(2.9802322387695303677E-08), \
    Decimal(1.4901161193847655147E-08), \
    Decimal(7.4505805969238279871E-09), \
    Decimal(3.7252902984619140453E-09), \
    Decimal(1.8626451492309570291E-09), \
    Decimal(9.3132257461547851536E-10), \
    Decimal(4.6566128730773925778E-10), \
    Decimal(2.3283064365386962890E-10), \
    Decimal(1.1641532182693481445E-10), \
    Decimal(5.8207660913467407226E-11), \
    Decimal(2.9103830456733703613E-11), \
    Decimal(1.4551915228366851807E-11), \
    Decimal(7.2759576141834259033E-12), \
    Decimal(3.6379788070917129517E-12), \
    Decimal(1.8189894035458564758E-12), \
    Decimal(9.0949470177292823792E-13), \
    Decimal(4.5474735088646411896E-13), \
    Decimal(2.2737367544323205948E-13), \
    Decimal(1.1368683772161602974E-13), \
    Decimal(5.6843418860808014870E-14), \
    Decimal(2.8421709430404007435E-14), \
    Decimal(1.4210854715202003717E-14), \
    Decimal(7.1054273576010018587E-15), \
    Decimal(3.5527136788005009294E-15), \
    Decimal(1.7763568394002504647E-15), \
    Decimal(8.8817841970012523234E-16), \
    Decimal(4.4408920985006261617E-16), \
    Decimal(2.2204460492503130808E-16), \
    Decimal(1.1102230246251565404E-16), \
    Decimal(5.5511151231257827021E-17), \
    Decimal(2.7755575615628913511E-17), \
    Decimal(1.3877787807814456755E-17), \
    Decimal(6.9388939039072283776E-18), \
    Decimal(3.4694469519536141888E-18), \
    Decimal(1.7347234759768070944E-18) ] )
  theta = Decimal(0)
  z = np.array ( [ Decimal(1), Decimal(0) ] )
  poweroftwo = Decimal(1)

  for j in range ( 0, n ):
    if ( z[1] < 0.0 ):
      sign_z2 = -1
    else:
      sign_z2 = +1
    if ( t <= z[0] ):
      sigma = + Decimal(sign_z2)
    else:
      sigma = - Decimal(sign_z2)
    if ( j < angles.size ):
      angle = Decimal(angles[j])
    else:
      angle = angle / Decimal(2)
    r = np.array ( [\
      [ Decimal(1), - sigma * poweroftwo ], \
      [ sigma * poweroftwo, Decimal(1) ] ] )
    z = np.dot ( r, np.dot ( r, z ) )
    theta+= Decimal(2) * sigma * angle
    t+= t * poweroftwo **2
    poweroftwo = poweroftwo / Decimal(2)
  return Decimal(theta)

def test(y):
    z=enc.cos(Decimal(y))
    return Decimal(arccos_cordic(z,70))

#stuck on 17 digits of precision
var=(test(1.1111111111111111))
