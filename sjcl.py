__all__ = ['sjcl']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['z', 'D', 'E', 'C', 'y', 'H', 'u', 'A', 'F', 'B', 'G', 't', 'sjcl'])
@Js
def PyJsHoisted_t_(a, b, c, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['p', 'w', 'e', 'q', 'h', 'k', 'l', 'f', 'g', 'x', 'v', 'b', 'c', 'a', 'r', 'n', 'm', 'd'])
    if PyJsStrictNeq(Js(4.0),var.get('b').get('length')):
        PyJsTempException = JsToPyException(var.get('sjcl').get('exception').get('invalid').create(Js('invalid aes block size')))
        raise PyJsTempException
    var.put('d', var.get('a').get('b').get(var.get('c')))
    var.put('e', (var.get('b').get('0')^var.get('d').get('0')))
    var.put('f', (var.get('b').get((Js(3.0) if var.get('c') else Js(1.0)))^var.get('d').get('1')))
    var.put('g', (var.get('b').get('2')^var.get('d').get('2')))
    var.put('b', (var.get('b').get((Js(1.0) if var.get('c') else Js(3.0)))^var.get('d').get('3')))
    var.put('n', ((var.get('d').get('length')/Js(4.0))-Js(2.0)))
    var.put('p', Js(4.0))
    var.put('r', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    var.put('h', var.get('a').get('s').get(var.get('c')))
    var.put('a', var.get('h').get('0'))
    var.put('q', var.get('h').get('1'))
    var.put('v', var.get('h').get('2'))
    var.put('w', var.get('h').get('3'))
    var.put('x', var.get('h').get('4'))
    #for JS loop
    var.put('m', Js(0.0))
    while (var.get('m')<var.get('n')):
        try:
            def PyJs_LONG_24_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('h', ((((var.get('a').get(PyJsBshift(var.get('e'),Js(24.0)))^var.get('q').get(((var.get('f')>>Js(16.0))&Js(255.0))))^var.get('v').get(((var.get('g')>>Js(8.0))&Js(255.0))))^var.get('w').get((var.get('b')&Js(255.0))))^var.get('d').get(var.get('p')))),var.put('k', ((((var.get('a').get(PyJsBshift(var.get('f'),Js(24.0)))^var.get('q').get(((var.get('g')>>Js(16.0))&Js(255.0))))^var.get('v').get(((var.get('b')>>Js(8.0))&Js(255.0))))^var.get('w').get((var.get('e')&Js(255.0))))^var.get('d').get((var.get('p')+Js(1.0)))))),var.put('l', ((((var.get('a').get(PyJsBshift(var.get('g'),Js(24.0)))^var.get('q').get(((var.get('b')>>Js(16.0))&Js(255.0))))^var.get('v').get(((var.get('e')>>Js(8.0))&Js(255.0))))^var.get('w').get((var.get('f')&Js(255.0))))^var.get('d').get((var.get('p')+Js(2.0)))))),var.put('b', ((((var.get('a').get(PyJsBshift(var.get('b'),Js(24.0)))^var.get('q').get(((var.get('e')>>Js(16.0))&Js(255.0))))^var.get('v').get(((var.get('f')>>Js(8.0))&Js(255.0))))^var.get('w').get((var.get('g')&Js(255.0))))^var.get('d').get((var.get('p')+Js(3.0)))))),var.put('p', Js(4.0), '+')),var.put('e', var.get('h'))),var.put('f', var.get('k'))),var.put('g', var.get('l')))
            PyJs_LONG_24_()
        finally:
                (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('m', Js(0.0))
    while (Js(4.0)>var.get('m')):
        try:
            def PyJs_LONG_25_(var=var):
                return var.get('r').put(((Js(3.0)&(-var.get('m'))) if var.get('c') else var.get('m')), (((((var.get('x').get(PyJsBshift(var.get('e'),Js(24.0)))<<Js(24.0))^(var.get('x').get(((var.get('f')>>Js(16.0))&Js(255.0)))<<Js(16.0)))^(var.get('x').get(((var.get('g')>>Js(8.0))&Js(255.0)))<<Js(8.0)))^var.get('x').get((var.get('b')&Js(255.0))))^var.get('d').get((var.put('p',Js(var.get('p').to_number())+Js(1))-Js(1)))))
            PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJs_LONG_25_(),var.put('h', var.get('e'))),var.put('e', var.get('f'))),var.put('f', var.get('g'))),var.put('g', var.get('b'))),var.put('b', var.get('h')))
        finally:
                (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1))
    return var.get('r')
PyJsHoisted_t_.func_name = 't'
var.put('t', PyJsHoisted_t_)
@Js
def PyJsHoisted_u_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['p', 'e', 'q', 'h', 'k', 'l', 'f', 'g', 'b', 'c', 'a', 'r', 'n', 'm', 'd'])
    var.put('f', var.get('a').get('F'))
    var.put('g', var.get('a').get('b'))
    var.put('h', var.get('f').get('0'))
    var.put('k', var.get('f').get('1'))
    var.put('l', var.get('f').get('2'))
    var.put('n', var.get('f').get('3'))
    var.put('m', var.get('f').get('4'))
    var.put('p', var.get('f').get('5'))
    var.put('r', var.get('f').get('6'))
    var.put('q', var.get('f').get('7'))
    #for JS loop
    var.put('c', Js(0.0))
    while (Js(64.0)>var.get('c')):
        try:
            def PyJs_LONG_66_(var=var):
                def PyJs_LONG_65_(var=var):
                    return (((((((PyJsBshift(var.get('d'),Js(7.0))^PyJsBshift(var.get('d'),Js(18.0)))^PyJsBshift(var.get('d'),Js(3.0)))^(var.get('d')<<Js(25.0)))^(var.get('d')<<Js(14.0)))+((((PyJsBshift(var.get('e'),Js(17.0))^PyJsBshift(var.get('e'),Js(19.0)))^PyJsBshift(var.get('e'),Js(10.0)))^(var.get('e')<<Js(15.0)))^(var.get('e')<<Js(13.0))))+var.get('b').get((var.get('c')&Js(15.0))))+var.get('b').get(((var.get('c')+Js(9.0))&Js(15.0))))
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma((var.put('d', var.get('b').get(var.get('c'))) if (Js(16.0)>var.get('c')) else PyJsComma(PyJsComma(var.put('d', var.get('b').get(((var.get('c')+Js(1.0))&Js(15.0)))),var.put('e', var.get('b').get(((var.get('c')+Js(14.0))&Js(15.0))))),var.put('d', var.get('b').put((var.get('c')&Js(15.0)), (PyJs_LONG_65_()|Js(0.0)))))),var.put('d', ((((var.get('d')+var.get('q'))+(((((PyJsBshift(var.get('m'),Js(6.0))^PyJsBshift(var.get('m'),Js(11.0)))^PyJsBshift(var.get('m'),Js(25.0)))^(var.get('m')<<Js(26.0)))^(var.get('m')<<Js(21.0)))^(var.get('m')<<Js(7.0))))+(var.get('r')^(var.get('m')&(var.get('p')^var.get('r')))))+var.get('g').get(var.get('c'))))),var.put('q', var.get('r'))),var.put('r', var.get('p'))),var.put('p', var.get('m'))),var.put('m', ((var.get('n')+var.get('d'))|Js(0.0)))),var.put('n', var.get('l'))),var.put('l', var.get('k'))),var.put('k', var.get('h'))),var.put('h', (((var.get('d')+((var.get('k')&var.get('l'))^(var.get('n')&(var.get('k')^var.get('l')))))+(((((PyJsBshift(var.get('k'),Js(2.0))^PyJsBshift(var.get('k'),Js(13.0)))^PyJsBshift(var.get('k'),Js(22.0)))^(var.get('k')<<Js(30.0)))^(var.get('k')<<Js(19.0)))^(var.get('k')<<Js(10.0))))|Js(0.0))))
            PyJs_LONG_66_()
        finally:
                (var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1))
    var.get('f').put('0', ((var.get('f').get('0')+var.get('h'))|Js(0.0)))
    var.get('f').put('1', ((var.get('f').get('1')+var.get('k'))|Js(0.0)))
    var.get('f').put('2', ((var.get('f').get('2')+var.get('l'))|Js(0.0)))
    var.get('f').put('3', ((var.get('f').get('3')+var.get('n'))|Js(0.0)))
    var.get('f').put('4', ((var.get('f').get('4')+var.get('m'))|Js(0.0)))
    var.get('f').put('5', ((var.get('f').get('5')+var.get('p'))|Js(0.0)))
    var.get('f').put('6', ((var.get('f').get('6')+var.get('r'))|Js(0.0)))
    var.get('f').put('7', ((var.get('f').get('7')+var.get('q'))|Js(0.0)))
PyJsHoisted_u_.func_name = 'u'
var.put('u', PyJsHoisted_u_)
@Js
def PyJsHoisted_A_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'b', 'c', 'a', 'd'])
    var.put('d', var.get('sjcl').get('random').get('K').get(var.get('a')))
    var.put('e', Js([]))
    for PyJsTemp in var.get('d'):
        var.put('c', PyJsTemp)
        (var.get('d').callprop('hasOwnProperty', var.get('c')) and var.get('e').callprop('push', var.get('d').get(var.get('c'))))
    #for JS loop
    var.put('c', Js(0.0))
    while (var.get('c')<var.get('e').get('length')):
        try:
            var.get('e').callprop(var.get('c'), var.get('b'))
        finally:
                (var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1))
PyJsHoisted_A_.func_name = 'A'
var.put('A', PyJsHoisted_A_)
@Js
def PyJsHoisted_C_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', 'b'])
    def PyJs_LONG_127_(var=var):
        return (var.get('a').callprop('addEntropy', var.get('window').get('performance').callprop('now'), var.get('b'), Js('loadtime')) if ((PyJsStrictNeq(Js('undefined'),var.get('window',throw=False).typeof()) and var.get('window').get('performance')) and PyJsStrictEq(Js('function'),var.get('window').get('performance').get('now').typeof())) else var.get('a').callprop('addEntropy', var.get('Date').create().callprop('valueOf'), var.get('b'), Js('loadtime')))
    PyJs_LONG_127_()
PyJsHoisted_C_.func_name = 'C'
var.put('C', PyJsHoisted_C_)
@Js
def PyJsHoisted_y_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    var.get('a').put('b', var.get('z')(var.get('a')).callprop('concat', var.get('z')(var.get('a'))))
    var.get('a').put('L', var.get('sjcl').get('cipher').get('aes').create(var.get('a').get('b')))
PyJsHoisted_y_.func_name = 'y'
var.put('y', PyJsHoisted_y_)
@Js
def PyJsHoisted_z_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', 'b'])
    #for JS loop
    var.put('b', Js(0.0))
    while ((Js(4.0)>var.get('b')) and PyJsComma(var.get('a').get('h').put(var.get('b'), ((var.get('a').get('h').get(var.get('b'))+Js(1.0))|Js(0.0))),var.get('a').get('h').get(var.get('b')).neg())):
        try:
            pass
        finally:
                (var.put('b',Js(var.get('b').to_number())+Js(1))-Js(1))
    return var.get('a').get('L').callprop('encrypt', var.get('a').get('h'))
PyJsHoisted_z_.func_name = 'z'
var.put('z', PyJsHoisted_z_)
@Js
def PyJsHoisted_B_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', 'b'])
    @Js
    def PyJs_anonymous_128_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        var.get('b').callprop('apply', var.get('a'), var.get('arguments'))
    PyJs_anonymous_128_._set_name('anonymous')
    return PyJs_anonymous_128_
PyJsHoisted_B_.func_name = 'B'
var.put('B', PyJsHoisted_B_)
Js('use strict')
PyJs_Object_1_ = Js({})
PyJs_Object_2_ = Js({})
PyJs_Object_3_ = Js({})
PyJs_Object_4_ = Js({})
PyJs_Object_5_ = Js({})
PyJs_Object_6_ = Js({})
@Js
def PyJs_anonymous_8_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    @Js
    def PyJs_anonymous_9_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        return (Js('CORRUPT: ')+var.get(u"this").get('message'))
    PyJs_anonymous_9_._set_name('anonymous')
    var.get(u"this").put('toString', PyJs_anonymous_9_)
    var.get(u"this").put('message', var.get('a'))
PyJs_anonymous_8_._set_name('anonymous')
@Js
def PyJs_anonymous_10_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    @Js
    def PyJs_anonymous_11_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        return (Js('INVALID: ')+var.get(u"this").get('message'))
    PyJs_anonymous_11_._set_name('anonymous')
    var.get(u"this").put('toString', PyJs_anonymous_11_)
    var.get(u"this").put('message', var.get('a'))
PyJs_anonymous_10_._set_name('anonymous')
@Js
def PyJs_anonymous_12_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    @Js
    def PyJs_anonymous_13_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        return (Js('BUG: ')+var.get(u"this").get('message'))
    PyJs_anonymous_13_._set_name('anonymous')
    var.get(u"this").put('toString', PyJs_anonymous_13_)
    var.get(u"this").put('message', var.get('a'))
PyJs_anonymous_12_._set_name('anonymous')
@Js
def PyJs_anonymous_14_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    @Js
    def PyJs_anonymous_15_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        return (Js('NOT READY: ')+var.get(u"this").get('message'))
    PyJs_anonymous_15_._set_name('anonymous')
    var.get(u"this").put('toString', PyJs_anonymous_15_)
    var.get(u"this").put('message', var.get('a'))
PyJs_anonymous_14_._set_name('anonymous')
PyJs_Object_7_ = Js({'corrupt':PyJs_anonymous_8_,'invalid':PyJs_anonymous_10_,'bug':PyJs_anonymous_12_,'notReady':PyJs_anonymous_14_})
PyJs_Object_0_ = Js({'cipher':PyJs_Object_1_,'hash':PyJs_Object_2_,'keyexchange':PyJs_Object_3_,'mode':PyJs_Object_4_,'misc':PyJs_Object_5_,'codec':PyJs_Object_6_,'exception':PyJs_Object_7_})
var.put('sjcl', PyJs_Object_0_)
@Js
def PyJs_anonymous_16_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'h', 'f', 'g', 'b', 'c', 'a', 'd'])
    (var.get(u"this").get('s').get('0').get('0').get('0') or var.get(u"this").callprop('O'))
    var.put('f', var.get(u"this").get('s').get('0').get('4'))
    var.put('g', var.get(u"this").get('s').get('1'))
    var.put('b', var.get('a').get('length'))
    var.put('h', Js(1.0))
    if ((PyJsStrictNeq(Js(4.0),var.get('b')) and PyJsStrictNeq(Js(6.0),var.get('b'))) and PyJsStrictNeq(Js(8.0),var.get('b'))):
        PyJsTempException = JsToPyException(var.get('sjcl').get('exception').get('invalid').create(Js('invalid aes key size')))
        raise PyJsTempException
    var.get(u"this").put('b', Js([var.put('d', var.get('a').callprop('slice', Js(0.0))), var.put('e', Js([]))]))
    #for JS loop
    var.put('a', var.get('b'))
    while (var.get('a')<((Js(4.0)*var.get('b'))+Js(28.0))):
        try:
            var.put('c', var.get('d').get((var.get('a')-Js(1.0))))
            if (PyJsStrictEq(Js(0.0),(var.get('a')%var.get('b'))) or (PyJsStrictEq(Js(8.0),var.get('b')) and PyJsStrictEq(Js(4.0),(var.get('a')%var.get('b'))))):
                def PyJs_LONG_17_(var=var):
                    return PyJsComma(var.put('c', ((((var.get('f').get(PyJsBshift(var.get('c'),Js(24.0)))<<Js(24.0))^(var.get('f').get(((var.get('c')>>Js(16.0))&Js(255.0)))<<Js(16.0)))^(var.get('f').get(((var.get('c')>>Js(8.0))&Js(255.0)))<<Js(8.0)))^var.get('f').get((var.get('c')&Js(255.0))))),(PyJsStrictEq(Js(0.0),(var.get('a')%var.get('b'))) and PyJsComma(var.put('c', (((var.get('c')<<Js(8.0))^PyJsBshift(var.get('c'),Js(24.0)))^(var.get('h')<<Js(24.0)))),var.put('h', ((var.get('h')<<Js(1.0))^(Js(283.0)*(var.get('h')>>Js(7.0))))))))
                PyJs_LONG_17_()
            var.get('d').put(var.get('a'), (var.get('d').get((var.get('a')-var.get('b')))^var.get('c')))
        finally:
                (var.put('a',Js(var.get('a').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('b', Js(0.0))
    while var.get('a'):
        try:
            def PyJs_LONG_18_(var=var):
                return var.get('e').put(var.get('b'), (var.get('c') if ((Js(4.0)>=var.get('a')) or (Js(4.0)>var.get('b'))) else (((var.get('g').get('0').get(var.get('f').get(PyJsBshift(var.get('c'),Js(24.0))))^var.get('g').get('1').get(var.get('f').get(((var.get('c')>>Js(16.0))&Js(255.0)))))^var.get('g').get('2').get(var.get('f').get(((var.get('c')>>Js(8.0))&Js(255.0)))))^var.get('g').get('3').get(var.get('f').get((var.get('c')&Js(255.0)))))))
            PyJsComma(var.put('c', var.get('d').get((var.get('a') if (var.get('b')&Js(3.0)) else (var.get('a')-Js(4.0))))),PyJs_LONG_18_())
        finally:
                PyJsComma((var.put('b',Js(var.get('b').to_number())+Js(1))-Js(1)),(var.put('a',Js(var.get('a').to_number())-Js(1))+Js(1)))
PyJs_anonymous_16_._set_name('anonymous')
var.get('sjcl').get('cipher').put('aes', PyJs_anonymous_16_)
@Js
def PyJs_anonymous_20_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    return var.get('t')(var.get(u"this"), var.get('a'), Js(0.0))
PyJs_anonymous_20_._set_name('anonymous')
@Js
def PyJs_anonymous_21_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    return var.get('t')(var.get(u"this"), var.get('a'), Js(1.0))
PyJs_anonymous_21_._set_name('anonymous')
@Js
def PyJs_anonymous_22_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['p', 'e', 'h', 'k', 'l', 'f', 'g', 'b', 'c', 'a', 'n', 'm', 'd'])
    var.put('a', var.get(u"this").get('s').get('0'))
    var.put('b', var.get(u"this").get('s').get('1'))
    var.put('c', var.get('a').get('4'))
    var.put('d', var.get('b').get('4'))
    var.put('h', Js([]))
    var.put('k', Js([]))
    #for JS loop
    var.put('e', Js(0.0))
    while (Js(256)>var.get('e')):
        try:
            var.get('k').put((var.get('h').put(var.get('e'), ((var.get('e')<<Js(1.0))^(Js(283.0)*(var.get('e')>>Js(7.0)))))^var.get('e')), var.get('e'))
        finally:
                (var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('f', var.put('g', Js(0.0)))
    while var.get('c').get(var.get('f')).neg():
        try:
            #for JS loop
            def PyJs_LONG_23_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.put('m', ((((var.get('g')^(var.get('g')<<Js(1.0)))^(var.get('g')<<Js(2.0)))^(var.get('g')<<Js(3.0)))^(var.get('g')<<Js(4.0)))),var.put('m', (((var.get('m')>>Js(8.0))^(var.get('m')&Js(255.0)))^Js(99.0)))),var.get('c').put(var.get('f'), var.get('m'))),var.get('d').put(var.get('m'), var.get('f'))),var.put('n', var.get('h').get(var.put('e', var.get('h').get(var.put('l', var.get('h').get(var.get('f')))))))),var.put('p', ((((Js(16843009)*var.get('n'))^(Js(65537)*var.get('e')))^(Js(257)*var.get('l')))^(Js(16843008)*var.get('f'))))),var.put('n', ((Js(257)*var.get('h').get(var.get('m')))^(Js(16843008)*var.get('m'))))),var.put('e', Js(0.0)))
            PyJs_LONG_23_()
            while (Js(4.0)>var.get('e')):
                try:
                    PyJsComma(var.get('a').get(var.get('e')).put(var.get('f'), var.put('n', ((var.get('n')<<Js(24.0))^PyJsBshift(var.get('n'),Js(8.0))))),var.get('b').get(var.get('e')).put(var.get('m'), var.put('p', ((var.get('p')<<Js(24.0))^PyJsBshift(var.get('p'),Js(8.0))))))
                finally:
                        (var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))
        finally:
                PyJsComma(var.put('f', (var.get('l') or Js(1.0)), '^'),var.put('g', (var.get('k').get(var.get('g')) or Js(1.0))))
    #for JS loop
    var.put('e', Js(0.0))
    while (Js(5.0)>var.get('e')):
        try:
            PyJsComma(var.get('a').put(var.get('e'), var.get('a').get(var.get('e')).callprop('slice', Js(0.0))),var.get('b').put(var.get('e'), var.get('b').get(var.get('e')).callprop('slice', Js(0.0))))
        finally:
                (var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))
PyJs_anonymous_22_._set_name('anonymous')
PyJs_Object_19_ = Js({'encrypt':PyJs_anonymous_20_,'decrypt':PyJs_anonymous_21_,'s':Js([Js([Js([]), Js([]), Js([]), Js([]), Js([])]), Js([Js([]), Js([]), Js([]), Js([]), Js([])])]),'O':PyJs_anonymous_22_})
var.get('sjcl').get('cipher').get('aes').put('prototype', PyJs_Object_19_)
pass
@Js
def PyJs_anonymous_27_(a, b, c, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['c', 'a', 'b'])
    var.put('a', var.get('sjcl').get('bitArray').callprop('$', var.get('a').callprop('slice', (var.get('b')/Js(32.0))), (Js(32.0)-(var.get('b')&Js(31.0)))).callprop('slice', Js(1.0)))
    return (var.get('a') if PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get('c')) else var.get('sjcl').get('bitArray').callprop('clamp', var.get('a'), (var.get('c')-var.get('b'))))
PyJs_anonymous_27_._set_name('anonymous')
@Js
def PyJs_anonymous_28_(a, b, c, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['c', 'a', 'b', 'd'])
    var.put('d', var.get('Math').callprop('floor', (((-var.get('b'))-var.get('c'))&Js(31.0))))
    return ((((var.get('a').get(((var.get('b')/Js(32.0))|Js(0.0)))<<(Js(32.0)-var.get('d')))^PyJsBshift(var.get('a').get((((var.get('b')/Js(32.0))+Js(1.0))|Js(0.0))),var.get('d'))) if ((((var.get('b')+var.get('c'))-Js(1.0))^var.get('b'))&(-Js(32.0))) else PyJsBshift(var.get('a').get(((var.get('b')/Js(32.0))|Js(0.0))),var.get('d')))&((Js(1.0)<<var.get('c'))-Js(1.0)))
PyJs_anonymous_28_._set_name('anonymous')
@Js
def PyJs_anonymous_29_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['c', 'a', 'b', 'd'])
    if (PyJsStrictEq(Js(0.0),var.get('a').get('length')) or PyJsStrictEq(Js(0.0),var.get('b').get('length'))):
        return var.get('a').callprop('concat', var.get('b'))
    var.put('c', var.get('a').get((var.get('a').get('length')-Js(1.0))))
    var.put('d', var.get('sjcl').get('bitArray').callprop('getPartial', var.get('c')))
    return (var.get('a').callprop('concat', var.get('b')) if PyJsStrictEq(Js(32.0),var.get('d')) else var.get('sjcl').get('bitArray').callprop('$', var.get('b'), var.get('d'), (var.get('c')|Js(0.0)), var.get('a').callprop('slice', Js(0.0), (var.get('a').get('length')-Js(1.0)))))
PyJs_anonymous_29_._set_name('anonymous')
@Js
def PyJs_anonymous_30_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', 'b'])
    var.put('b', var.get('a').get('length'))
    return (Js(0.0) if PyJsStrictEq(Js(0.0),var.get('b')) else ((Js(32.0)*(var.get('b')-Js(1.0)))+var.get('sjcl').get('bitArray').callprop('getPartial', var.get('a').get((var.get('b')-Js(1.0))))))
PyJs_anonymous_30_._set_name('anonymous')
@Js
def PyJs_anonymous_31_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['c', 'a', 'b'])
    if ((Js(32.0)*var.get('a').get('length'))<var.get('b')):
        return var.get('a')
    var.put('a', var.get('a').callprop('slice', Js(0.0), var.get('Math').callprop('ceil', (var.get('b')/Js(32.0)))))
    var.put('c', var.get('a').get('length'))
    var.put('b', (var.get('b')&Js(31.0)))
    (((Js(0.0)<var.get('c')) and var.get('b')) and var.get('a').put((var.get('c')-Js(1.0)), var.get('sjcl').get('bitArray').callprop('partial', var.get('b'), (var.get('a').get((var.get('c')-Js(1.0)))&(Js(2147483648.0)>>(var.get('b')-Js(1.0)))), Js(1.0))))
    return var.get('a')
PyJs_anonymous_31_._set_name('anonymous')
@Js
def PyJs_anonymous_32_(a, b, c, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['c', 'a', 'b'])
    return (var.get('b') if PyJsStrictEq(Js(32.0),var.get('a')) else (((var.get('b')|Js(0.0)) if var.get('c') else (var.get('b')<<(Js(32.0)-var.get('a'))))+(Js(1099511627776)*var.get('a'))))
PyJs_anonymous_32_._set_name('anonymous')
@Js
def PyJs_anonymous_33_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    return (var.get('Math').callprop('round', (var.get('a')/Js(1099511627776))) or Js(32.0))
PyJs_anonymous_33_._set_name('anonymous')
@Js
def PyJs_anonymous_34_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['c', 'a', 'b', 'd'])
    if PyJsStrictNeq(var.get('sjcl').get('bitArray').callprop('bitLength', var.get('a')),var.get('sjcl').get('bitArray').callprop('bitLength', var.get('b'))):
        return Js(1.0).neg()
    var.put('c', Js(0.0))
    #for JS loop
    var.put('d', Js(0.0))
    while (var.get('d')<var.get('a').get('length')):
        try:
            var.put('c', (var.get('a').get(var.get('d'))^var.get('b').get(var.get('d'))), '|')
        finally:
                (var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1))
    return PyJsStrictEq(Js(0.0),var.get('c'))
PyJs_anonymous_34_._set_name('anonymous')
@Js
def PyJs_anonymous_35_(a, b, c, d, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'b', 'c', 'a', 'd'])
    pass
    var.put('e', Js(0.0))
    #for JS loop
    (PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get('d')) and var.put('d', Js([])))
    while (Js(32.0)<=var.get('b')):
        try:
            PyJsComma(var.get('d').callprop('push', var.get('c')),var.put('c', Js(0.0)))
        finally:
                var.put('b', Js(32.0), '-')
    if PyJsStrictEq(Js(0.0),var.get('b')):
        return var.get('d').callprop('concat', var.get('a'))
    #for JS loop
    var.put('e', Js(0.0))
    while (var.get('e')<var.get('a').get('length')):
        try:
            PyJsComma(var.get('d').callprop('push', (var.get('c')|PyJsBshift(var.get('a').get(var.get('e')),var.get('b')))),var.put('c', (var.get('a').get(var.get('e'))<<(Js(32.0)-var.get('b')))))
        finally:
                (var.put('e',Js(var.get('e').to_number())+Js(1))-Js(1))
    var.put('e', (var.get('a').get((var.get('a').get('length')-Js(1.0))) if var.get('a').get('length') else Js(0.0)))
    var.put('a', var.get('sjcl').get('bitArray').callprop('getPartial', var.get('e')))
    var.get('d').callprop('push', var.get('sjcl').get('bitArray').callprop('partial', ((var.get('b')+var.get('a'))&Js(31.0)), (var.get('c') if (Js(32.0)<(var.get('b')+var.get('a'))) else var.get('d').callprop('pop')), Js(1.0)))
    return var.get('d')
PyJs_anonymous_35_._set_name('anonymous')
@Js
def PyJs_anonymous_36_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', 'b'])
    return Js([(var.get('a').get('0')^var.get('b').get('0')), (var.get('a').get('1')^var.get('b').get('1')), (var.get('a').get('2')^var.get('b').get('2')), (var.get('a').get('3')^var.get('b').get('3'))])
PyJs_anonymous_36_._set_name('anonymous')
@Js
def PyJs_anonymous_37_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['c', 'a', 'b'])
    pass
    #for JS loop
    var.put('b', Js(0.0))
    while (var.get('b')<var.get('a').get('length')):
        try:
            PyJsComma(var.put('c', var.get('a').get(var.get('b'))),var.get('a').put(var.get('b'), (((PyJsBshift(var.get('c'),Js(24.0))|(PyJsBshift(var.get('c'),Js(8.0))&Js(65280)))|((var.get('c')&Js(65280))<<Js(8.0)))|(var.get('c')<<Js(24.0)))))
        finally:
                var.put('b',Js(var.get('b').to_number())+Js(1))
    return var.get('a')
PyJs_anonymous_37_._set_name('anonymous')
PyJs_Object_26_ = Js({'bitSlice':PyJs_anonymous_27_,'extract':PyJs_anonymous_28_,'concat':PyJs_anonymous_29_,'bitLength':PyJs_anonymous_30_,'clamp':PyJs_anonymous_31_,'partial':PyJs_anonymous_32_,'getPartial':PyJs_anonymous_33_,'equal':PyJs_anonymous_34_,'$':PyJs_anonymous_35_,'i':PyJs_anonymous_36_,'byteswapM':PyJs_anonymous_37_})
var.get('sjcl').put('bitArray', PyJs_Object_26_)
@Js
def PyJs_anonymous_39_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'b', 'c', 'a', 'd'])
    var.put('b', Js(''))
    var.put('c', var.get('sjcl').get('bitArray').callprop('bitLength', var.get('a')))
    #for JS loop
    var.put('d', Js(0.0))
    while (var.get('d')<(var.get('c')/Js(8.0))):
        try:
            PyJsComma(PyJsComma((PyJsStrictEq(Js(0.0),(var.get('d')&Js(3.0))) and var.put('e', var.get('a').get((var.get('d')/Js(4.0))))),var.put('b', var.get('String').callprop('fromCharCode', PyJsBshift(PyJsBshift(PyJsBshift(var.get('e'),Js(8.0)),Js(8.0)),Js(8.0))), '+')),var.put('e', Js(8.0), '<<'))
        finally:
                (var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1))
    return var.get('decodeURIComponent')(var.get('escape')(var.get('b')))
PyJs_anonymous_39_._set_name('anonymous')
@Js
def PyJs_anonymous_40_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['c', 'a', 'b', 'd'])
    var.put('a', var.get('unescape')(var.get('encodeURIComponent')(var.get('a'))))
    var.put('b', Js([]))
    var.put('d', Js(0.0))
    #for JS loop
    var.put('c', Js(0.0))
    while (var.get('c')<var.get('a').get('length')):
        try:
            PyJsComma(var.put('d', ((var.get('d')<<Js(8.0))|var.get('a').callprop('charCodeAt', var.get('c')))),(PyJsStrictEq(Js(3.0),(var.get('c')&Js(3.0))) and PyJsComma(var.get('b').callprop('push', var.get('d')),var.put('d', Js(0.0)))))
        finally:
                (var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1))
    ((var.get('c')&Js(3.0)) and var.get('b').callprop('push', var.get('sjcl').get('bitArray').callprop('partial', (Js(8.0)*(var.get('c')&Js(3.0))), var.get('d'))))
    return var.get('b')
PyJs_anonymous_40_._set_name('anonymous')
PyJs_Object_38_ = Js({'fromBits':PyJs_anonymous_39_,'toBits':PyJs_anonymous_40_})
var.get('sjcl').get('codec').put('utf8String', PyJs_Object_38_)
@Js
def PyJs_anonymous_42_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['c', 'a', 'b'])
    var.put('b', Js(''))
    #for JS loop
    var.put('c', Js(0.0))
    while (var.get('c')<var.get('a').get('length')):
        try:
            var.put('b', ((var.get('a').get(var.get('c'))|Js(0.0))+Js(263882790666240)).callprop('toString', Js(16.0)).callprop('substr', Js(4.0)), '+')
        finally:
                (var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1))
    return var.get('b').callprop('substr', Js(0.0), (var.get('sjcl').get('bitArray').callprop('bitLength', var.get('a'))/Js(4.0)))
PyJs_anonymous_42_._set_name('anonymous')
@Js
def PyJs_anonymous_43_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['c', 'a', 'b', 'd'])
    var.put('c', Js([]))
    var.put('a', var.get('a').callprop('replace', JsRegExp('/\\s|0x/g'), Js('')))
    var.put('d', var.get('a').get('length'))
    var.put('a', (var.get('a')+Js('00000000')))
    #for JS loop
    var.put('b', Js(0.0))
    while (var.get('b')<var.get('a').get('length')):
        try:
            var.get('c').callprop('push', (var.get('parseInt')(var.get('a').callprop('substr', var.get('b'), Js(8.0)), Js(16.0))^Js(0.0)))
        finally:
                var.put('b', Js(8.0), '+')
    return var.get('sjcl').get('bitArray').callprop('clamp', var.get('c'), (Js(4.0)*var.get('d')))
PyJs_anonymous_43_._set_name('anonymous')
PyJs_Object_41_ = Js({'fromBits':PyJs_anonymous_42_,'toBits':PyJs_anonymous_43_})
var.get('sjcl').get('codec').put('hex', PyJs_Object_41_)
@Js
def PyJs_anonymous_45_(a, b, c, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'h', 'k', 'l', 'f', 'g', 'b', 'c', 'a', 'd'])
    var.put('d', var.get('sjcl').get('codec').get('base32').get('BASE'))
    var.put('e', var.get('sjcl').get('codec').get('base32').get('REMAINING'))
    var.put('f', Js(''))
    var.put('g', Js(0.0))
    var.put('h', var.get('sjcl').get('codec').get('base32').get('B'))
    var.put('k', Js(0.0))
    var.put('l', var.get('sjcl').get('bitArray').callprop('bitLength', var.get('a')))
    (var.get('c') and var.put('h', var.get('sjcl').get('codec').get('base32').get('X')))
    #for JS loop
    var.put('c', Js(0.0))
    while ((var.get('f').get('length')*var.get('d'))<var.get('l')):
        def PyJs_LONG_46_(var=var):
            return PyJsComma(var.put('f', var.get('h').callprop('charAt', PyJsBshift((var.get('k')^PyJsBshift(var.get('a').get(var.get('c')),var.get('g'))),var.get('e'))), '+'),(PyJsComma(PyJsComma(var.put('k', (var.get('a').get(var.get('c'))<<(var.get('d')-var.get('g')))),var.put('g', var.get('e'), '+')),(var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1))) if (var.get('g')<var.get('d')) else PyJsComma(var.put('k', var.get('d'), '<<'),var.put('g', var.get('d'), '-'))))
        PyJs_LONG_46_()
    
    #for JS loop
    
    while ((var.get('f').get('length')&Js(7.0)) and var.get('b').neg()):
        var.put('f', Js('='), '+')
    
    return var.get('f')
PyJs_anonymous_45_._set_name('anonymous')
@Js
def PyJs_anonymous_47_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'h', 'k', 'l', 'f', 'g', 'b', 'c', 'a', 'n', 'm', 'd'])
    var.put('a', var.get('a').callprop('replace', JsRegExp('/\\s|=/g'), Js('')).callprop('toUpperCase'))
    var.put('c', var.get('sjcl').get('codec').get('base32').get('BITS'))
    var.put('d', var.get('sjcl').get('codec').get('base32').get('BASE'))
    var.put('e', var.get('sjcl').get('codec').get('base32').get('REMAINING'))
    var.put('f', Js([]))
    var.put('h', Js(0.0))
    var.put('k', var.get('sjcl').get('codec').get('base32').get('B'))
    var.put('l', Js(0.0))
    var.put('m', Js('base32'))
    (var.get('b') and PyJsComma(var.put('k', var.get('sjcl').get('codec').get('base32').get('X')),var.put('m', Js('base32hex'))))
    #for JS loop
    var.put('g', Js(0.0))
    while (var.get('g')<var.get('a').get('length')):
        try:
            var.put('n', var.get('k').callprop('indexOf', var.get('a').callprop('charAt', var.get('g'))))
            if (Js(0.0)>var.get('n')):
                if var.get('b').neg():
                    try:
                        return var.get('sjcl').get('codec').get('base32hex').callprop('toBits', var.get('a'))
                    except PyJsException as PyJsTempException:
                        PyJsHolder_70_74370291 = var.own.get('p')
                        var.force_own_put('p', PyExceptionToJs(PyJsTempException))
                        try:
                            pass
                        finally:
                            if PyJsHolder_70_74370291 is not None:
                                var.own['p'] = PyJsHolder_70_74370291
                            else:
                                del var.own['p']
                            del PyJsHolder_70_74370291
                PyJsTempException = JsToPyException(var.get('sjcl').get('exception').get('invalid').create(((Js("this isn't ")+var.get('m'))+Js('!'))))
                raise PyJsTempException
            (PyJsComma(PyJsComma(var.put('h', var.get('e'), '-'),var.get('f').callprop('push', (var.get('l')^PyJsBshift(var.get('n'),var.get('h'))))),var.put('l', (var.get('n')<<(var.get('c')-var.get('h'))))) if (var.get('h')>var.get('e')) else PyJsComma(var.put('h', var.get('d'), '+'),var.put('l', (var.get('n')<<(var.get('c')-var.get('h'))), '^')))
        finally:
                (var.put('g',Js(var.get('g').to_number())+Js(1))-Js(1))
    ((var.get('h')&Js(56.0)) and var.get('f').callprop('push', var.get('sjcl').get('bitArray').callprop('partial', (var.get('h')&Js(56.0)), var.get('l'), Js(1.0))))
    return var.get('f')
PyJs_anonymous_47_._set_name('anonymous')
PyJs_Object_44_ = Js({'B':Js('ABCDEFGHIJKLMNOPQRSTUVWXYZ234567'),'X':Js('0123456789ABCDEFGHIJKLMNOPQRSTUV'),'BITS':Js(32.0),'BASE':Js(5.0),'REMAINING':Js(27.0),'fromBits':PyJs_anonymous_45_,'toBits':PyJs_anonymous_47_})
var.get('sjcl').get('codec').put('base32', PyJs_Object_44_)
@Js
def PyJs_anonymous_49_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', 'b'])
    return var.get('sjcl').get('codec').get('base32').callprop('fromBits', var.get('a'), var.get('b'), Js(1.0))
PyJs_anonymous_49_._set_name('anonymous')
@Js
def PyJs_anonymous_50_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    return var.get('sjcl').get('codec').get('base32').callprop('toBits', var.get('a'), Js(1.0))
PyJs_anonymous_50_._set_name('anonymous')
PyJs_Object_48_ = Js({'fromBits':PyJs_anonymous_49_,'toBits':PyJs_anonymous_50_})
var.get('sjcl').get('codec').put('base32hex', PyJs_Object_48_)
@Js
def PyJs_anonymous_52_(a, b, c, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'h', 'f', 'g', 'b', 'c', 'a', 'd'])
    var.put('d', Js(''))
    var.put('e', Js(0.0))
    var.put('f', var.get('sjcl').get('codec').get('base64').get('B'))
    var.put('g', Js(0.0))
    var.put('h', var.get('sjcl').get('bitArray').callprop('bitLength', var.get('a')))
    (var.get('c') and var.put('f', (var.get('f').callprop('substr', Js(0.0), Js(62.0))+Js('-_'))))
    #for JS loop
    var.put('c', Js(0.0))
    while ((Js(6.0)*var.get('d').get('length'))<var.get('h')):
        def PyJs_LONG_53_(var=var):
            return PyJsComma(var.put('d', var.get('f').callprop('charAt', PyJsBshift((var.get('g')^PyJsBshift(var.get('a').get(var.get('c')),var.get('e'))),Js(26.0))), '+'),(PyJsComma(PyJsComma(var.put('g', (var.get('a').get(var.get('c'))<<(Js(6.0)-var.get('e')))),var.put('e', Js(26.0), '+')),(var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1))) if (Js(6.0)>var.get('e')) else PyJsComma(var.put('g', Js(6.0), '<<'),var.put('e', Js(6.0), '-'))))
        PyJs_LONG_53_()
    
    #for JS loop
    
    while ((var.get('d').get('length')&Js(3.0)) and var.get('b').neg()):
        var.put('d', Js('='), '+')
    
    return var.get('d')
PyJs_anonymous_52_._set_name('anonymous')
@Js
def PyJs_anonymous_54_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'h', 'f', 'g', 'b', 'c', 'a', 'd'])
    var.put('a', var.get('a').callprop('replace', JsRegExp('/\\s|=/g'), Js('')))
    var.put('c', Js([]))
    var.put('e', Js(0.0))
    var.put('f', var.get('sjcl').get('codec').get('base64').get('B'))
    var.put('g', Js(0.0))
    (var.get('b') and var.put('f', (var.get('f').callprop('substr', Js(0.0), Js(62.0))+Js('-_'))))
    #for JS loop
    var.put('d', Js(0.0))
    while (var.get('d')<var.get('a').get('length')):
        try:
            var.put('h', var.get('f').callprop('indexOf', var.get('a').callprop('charAt', var.get('d'))))
            if (Js(0.0)>var.get('h')):
                PyJsTempException = JsToPyException(var.get('sjcl').get('exception').get('invalid').create(Js("this isn't base64!")))
                raise PyJsTempException
            (PyJsComma(PyJsComma(var.put('e', Js(26.0), '-'),var.get('c').callprop('push', (var.get('g')^PyJsBshift(var.get('h'),var.get('e'))))),var.put('g', (var.get('h')<<(Js(32.0)-var.get('e'))))) if (Js(26.0)<var.get('e')) else PyJsComma(var.put('e', Js(6.0), '+'),var.put('g', (var.get('h')<<(Js(32.0)-var.get('e'))), '^')))
        finally:
                (var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1))
    ((var.get('e')&Js(56.0)) and var.get('c').callprop('push', var.get('sjcl').get('bitArray').callprop('partial', (var.get('e')&Js(56.0)), var.get('g'), Js(1.0))))
    return var.get('c')
PyJs_anonymous_54_._set_name('anonymous')
PyJs_Object_51_ = Js({'B':Js('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'),'fromBits':PyJs_anonymous_52_,'toBits':PyJs_anonymous_54_})
var.get('sjcl').get('codec').put('base64', PyJs_Object_51_)
@Js
def PyJs_anonymous_56_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    return var.get('sjcl').get('codec').get('base64').callprop('fromBits', var.get('a'), Js(1.0), Js(1.0))
PyJs_anonymous_56_._set_name('anonymous')
@Js
def PyJs_anonymous_57_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    return var.get('sjcl').get('codec').get('base64').callprop('toBits', var.get('a'), Js(1.0))
PyJs_anonymous_57_._set_name('anonymous')
PyJs_Object_55_ = Js({'fromBits':PyJs_anonymous_56_,'toBits':PyJs_anonymous_57_})
var.get('sjcl').get('codec').put('base64url', PyJs_Object_55_)
@Js
def PyJs_anonymous_58_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    (var.get(u"this").get('b').get('0') or var.get(u"this").callprop('O'))
    (PyJsComma(PyJsComma(var.get(u"this").put('F', var.get('a').get('F').callprop('slice', Js(0.0))),var.get(u"this").put('A', var.get('a').get('A').callprop('slice', Js(0.0)))),var.get(u"this").put('l', var.get('a').get('l'))) if var.get('a') else var.get(u"this").callprop('reset'))
PyJs_anonymous_58_._set_name('anonymous')
var.get('sjcl').get('hash').put('sha256', PyJs_anonymous_58_)
@Js
def PyJs_anonymous_59_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    return var.get('sjcl').get('hash').get('sha256').create().callprop('update', var.get('a')).callprop('finalize')
PyJs_anonymous_59_._set_name('anonymous')
var.get('sjcl').get('hash').get('sha256').put('hash', PyJs_anonymous_59_)
@Js
def PyJs_anonymous_61_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    var.get(u"this").put('F', var.get(u"this").get('Y').callprop('slice', Js(0.0)))
    var.get(u"this").put('A', Js([]))
    var.get(u"this").put('l', Js(0.0))
    return var.get(u"this")
PyJs_anonymous_61_._set_name('anonymous')
@Js
def PyJs_anonymous_62_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'b', 'c', 'a', 'd'])
    (PyJsStrictEq(Js('string'),var.get('a',throw=False).typeof()) and var.put('a', var.get('sjcl').get('codec').get('utf8String').callprop('toBits', var.get('a'))))
    var.put('c', var.get(u"this").put('A', var.get('sjcl').get('bitArray').callprop('concat', var.get(u"this").get('A'), var.get('a'))))
    var.put('b', var.get(u"this").get('l'))
    var.put('a', var.get(u"this").put('l', (var.get('b')+var.get('sjcl').get('bitArray').callprop('bitLength', var.get('a')))))
    if (Js(9007199254740991)<var.get('a')):
        PyJsTempException = JsToPyException(var.get('sjcl').get('exception').get('invalid').create(Js('Cannot hash more than 2^53 - 1 bits')))
        raise PyJsTempException
    if PyJsStrictNeq(Js('undefined'),var.get('Uint32Array',throw=False).typeof()):
        var.put('d', var.get('Uint32Array').create(var.get('c')))
        var.put('e', Js(0.0))
        #for JS loop
        var.put('b', ((Js(512.0)+var.get('b'))-((Js(512.0)+var.get('b'))&Js(511))))
        while (var.get('b')<=var.get('a')):
            try:
                PyJsComma(var.get('u')(var.get(u"this"), var.get('d').callprop('subarray', (Js(16.0)*var.get('e')), (Js(16.0)*(var.get('e')+Js(1.0))))),var.put('e', Js(1.0), '+'))
            finally:
                    var.put('b', Js(512.0), '+')
        var.get('c').callprop('splice', Js(0.0), (Js(16.0)*var.get('e')))
    else:
        #for JS loop
        var.put('b', ((Js(512.0)+var.get('b'))-((Js(512.0)+var.get('b'))&Js(511))))
        while (var.get('b')<=var.get('a')):
            try:
                var.get('u')(var.get(u"this"), var.get('c').callprop('splice', Js(0.0), Js(16.0)))
            finally:
                    var.put('b', Js(512.0), '+')
    return var.get(u"this")
PyJs_anonymous_62_._set_name('anonymous')
@Js
def PyJs_anonymous_63_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['c', 'a', 'b'])
    var.put('b', var.get(u"this").get('A'))
    var.put('c', var.get(u"this").get('F'))
    var.put('b', var.get('sjcl').get('bitArray').callprop('concat', var.get('b'), Js([var.get('sjcl').get('bitArray').callprop('partial', Js(1.0), Js(1.0))])))
    #for JS loop
    var.put('a', (var.get('b').get('length')+Js(2.0)))
    while (var.get('a')&Js(15.0)):
        try:
            var.get('b').callprop('push', Js(0.0))
        finally:
                (var.put('a',Js(var.get('a').to_number())+Js(1))-Js(1))
    var.get('b').callprop('push', var.get('Math').callprop('floor', (var.get(u"this").get('l')/Js(4294967296))))
    #for JS loop
    var.get('b').callprop('push', (var.get(u"this").get('l')|Js(0.0)))
    while var.get('b').get('length'):
        var.get('u')(var.get(u"this"), var.get('b').callprop('splice', Js(0.0), Js(16.0)))
    
    var.get(u"this").callprop('reset')
    return var.get('c')
PyJs_anonymous_63_._set_name('anonymous')
@Js
def PyJs_anonymous_64_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'b', 'c', 'a', 'd'])
    @Js
    def PyJsHoisted_a_(a, this, arguments, var=var):
        var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['a'])
        return ((Js(4294967296)*(var.get('a')-var.get('Math').callprop('floor', var.get('a'))))|Js(0.0))
    PyJsHoisted_a_.func_name = 'a'
    var.put('a', PyJsHoisted_a_)
    pass
    #for JS loop
    var.put('b', Js(0.0))
    var.put('c', Js(2.0))
    while (Js(64.0)>var.get('b')):
        try:
            var.put('e', Js(0.0).neg())
            #for JS loop
            var.put('d', Js(2.0))
            while ((var.get('d')*var.get('d'))<=var.get('c')):
                try:
                    if PyJsStrictEq(Js(0.0),(var.get('c')%var.get('d'))):
                        var.put('e', Js(1.0).neg())
                        break
                finally:
                        (var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1))
            (var.get('e') and PyJsComma(PyJsComma(((Js(8.0)>var.get('b')) and var.get(u"this").get('Y').put(var.get('b'), var.get('a')(var.get('Math').callprop('pow', var.get('c'), Js(0.5))))),var.get(u"this").get('b').put(var.get('b'), var.get('a')(var.get('Math').callprop('pow', var.get('c'), (Js(1.0)/Js(3.0)))))),(var.put('b',Js(var.get('b').to_number())+Js(1))-Js(1))))
        finally:
                (var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1))
PyJs_anonymous_64_._set_name('anonymous')
PyJs_Object_60_ = Js({'blockSize':Js(512.0),'reset':PyJs_anonymous_61_,'update':PyJs_anonymous_62_,'finalize':PyJs_anonymous_63_,'Y':Js([]),'b':Js([]),'O':PyJs_anonymous_64_})
var.get('sjcl').get('hash').get('sha256').put('prototype', PyJs_Object_60_)
pass
@Js
def PyJs_anonymous_68_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    var.get('sjcl').get('mode').get('ccm').get('G').callprop('push', var.get('a'))
PyJs_anonymous_68_._set_name('anonymous')
@Js
def PyJs_anonymous_69_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    var.put('a', var.get('sjcl').get('mode').get('ccm').get('G').callprop('indexOf', var.get('a')))
    (((-Js(1.0))<var.get('a')) and var.get('sjcl').get('mode').get('ccm').get('G').callprop('splice', var.get('a'), Js(1.0)))
PyJs_anonymous_69_._set_name('anonymous')
@Js
def PyJs_anonymous_70_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['c', 'a', 'b'])
    var.put('b', var.get('sjcl').get('mode').get('ccm').get('G').callprop('slice'))
    #for JS loop
    var.put('c', Js(0.0))
    while (var.get('c')<var.get('b').get('length')):
        try:
            var.get('b').callprop(var.get('c'), var.get('a'))
        finally:
                var.put('c', Js(1.0), '+')
PyJs_anonymous_70_._set_name('anonymous')
@Js
def PyJs_anonymous_71_(a, b, c, d, e, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'h', 'k', 'l', 'f', 'g', 'b', 'c', 'a', 'd'])
    var.put('g', var.get('b').callprop('slice', Js(0.0)))
    var.put('h', var.get('sjcl').get('bitArray'))
    var.put('k', (var.get('h').callprop('bitLength', var.get('c'))/Js(8.0)))
    var.put('l', (var.get('h').callprop('bitLength', var.get('g'))/Js(8.0)))
    var.put('e', (var.get('e') or Js(64.0)))
    var.put('d', (var.get('d') or Js([])))
    if (Js(7.0)>var.get('k')):
        PyJsTempException = JsToPyException(var.get('sjcl').get('exception').get('invalid').create(Js('ccm: iv must be at least 7 bytes')))
        raise PyJsTempException
    #for JS loop
    var.put('f', Js(2.0))
    while ((Js(4.0)>var.get('f')) and PyJsBshift(var.get('l'),(Js(8.0)*var.get('f')))):
        try:
            pass
        finally:
                (var.put('f',Js(var.get('f').to_number())+Js(1))-Js(1))
    ((var.get('f')<(Js(15.0)-var.get('k'))) and var.put('f', (Js(15.0)-var.get('k'))))
    var.put('c', var.get('h').callprop('clamp', var.get('c'), (Js(8.0)*(Js(15.0)-var.get('f')))))
    var.put('b', var.get('sjcl').get('mode').get('ccm').callprop('V', var.get('a'), var.get('b'), var.get('c'), var.get('d'), var.get('e'), var.get('f')))
    var.put('g', var.get('sjcl').get('mode').get('ccm').callprop('C', var.get('a'), var.get('g'), var.get('c'), var.get('b'), var.get('e'), var.get('f')))
    return var.get('h').callprop('concat', var.get('g').get('data'), var.get('g').get('tag'))
PyJs_anonymous_71_._set_name('anonymous')
@Js
def PyJs_anonymous_72_(a, b, c, d, e, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'h', 'k', 'l', 'f', 'g', 'b', 'c', 'a', 'd'])
    var.put('e', (var.get('e') or Js(64.0)))
    var.put('d', (var.get('d') or Js([])))
    var.put('f', var.get('sjcl').get('bitArray'))
    var.put('g', (var.get('f').callprop('bitLength', var.get('c'))/Js(8.0)))
    var.put('h', var.get('f').callprop('bitLength', var.get('b')))
    var.put('k', var.get('f').callprop('clamp', var.get('b'), (var.get('h')-var.get('e'))))
    var.put('l', var.get('f').callprop('bitSlice', var.get('b'), (var.get('h')-var.get('e'))))
    var.put('h', ((var.get('h')-var.get('e'))/Js(8.0)))
    if (Js(7.0)>var.get('g')):
        PyJsTempException = JsToPyException(var.get('sjcl').get('exception').get('invalid').create(Js('ccm: iv must be at least 7 bytes')))
        raise PyJsTempException
    #for JS loop
    var.put('b', Js(2.0))
    while ((Js(4.0)>var.get('b')) and PyJsBshift(var.get('h'),(Js(8.0)*var.get('b')))):
        try:
            pass
        finally:
                (var.put('b',Js(var.get('b').to_number())+Js(1))-Js(1))
    ((var.get('b')<(Js(15.0)-var.get('g'))) and var.put('b', (Js(15.0)-var.get('g'))))
    var.put('c', var.get('f').callprop('clamp', var.get('c'), (Js(8.0)*(Js(15.0)-var.get('b')))))
    var.put('k', var.get('sjcl').get('mode').get('ccm').callprop('C', var.get('a'), var.get('k'), var.get('c'), var.get('l'), var.get('e'), var.get('b')))
    var.put('a', var.get('sjcl').get('mode').get('ccm').callprop('V', var.get('a'), var.get('k').get('data'), var.get('c'), var.get('d'), var.get('e'), var.get('b')))
    if var.get('f').callprop('equal', var.get('k').get('tag'), var.get('a')).neg():
        PyJsTempException = JsToPyException(var.get('sjcl').get('exception').get('corrupt').create(Js("ccm: tag doesn't match")))
        raise PyJsTempException
    return var.get('k').get('data')
PyJs_anonymous_72_._set_name('anonymous')
@Js
def PyJs_anonymous_73_(a, b, c, d, e, f, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'e':e, 'f':f, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'h', 'k', 'f', 'g', 'b', 'c', 'a', 'd'])
    var.put('g', Js([]))
    var.put('h', var.get('sjcl').get('bitArray'))
    var.put('k', var.get('h').get('i'))
    var.put('d', Js([var.get('h').callprop('partial', Js(8.0), (((Js(64.0) if var.get('b').get('length') else Js(0.0))|((var.get('d')-Js(2.0))<<Js(2.0)))|(var.get('f')-Js(1.0))))]))
    var.put('d', var.get('h').callprop('concat', var.get('d'), var.get('c')))
    var.get('d').put('3', var.get('e'), '|')
    var.put('d', var.get('a').callprop('encrypt', var.get('d')))
    if var.get('b').get('length'):
        #for JS loop
        def PyJs_LONG_74_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(var.put('c', (var.get('h').callprop('bitLength', var.get('b'))/Js(8.0))),(var.put('g', Js([var.get('h').callprop('partial', Js(16.0), var.get('c'))])) if (Js(65279.0)>=var.get('c')) else ((Js(4294967295)>=var.get('c')) and var.put('g', var.get('h').callprop('concat', Js([var.get('h').callprop('partial', Js(16.0), Js(65534.0))]), Js([var.get('c')])))))),var.put('g', var.get('h').callprop('concat', var.get('g'), var.get('b')))),var.put('b', Js(0.0)))
        PyJs_LONG_74_()
        while (var.get('b')<var.get('g').get('length')):
            try:
                var.put('d', var.get('a').callprop('encrypt', var.get('k')(var.get('d'), var.get('g').callprop('slice', var.get('b'), (var.get('b')+Js(4.0))).callprop('concat', Js([Js(0.0), Js(0.0), Js(0.0)])))))
            finally:
                    var.put('b', Js(4.0), '+')
    return var.get('d')
PyJs_anonymous_73_._set_name('anonymous')
@Js
def PyJs_anonymous_75_(a, b, c, d, e, f, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'e':e, 'f':f, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'h', 'f', 'g', 'b', 'c', 'a', 'd'])
    var.put('g', var.get('sjcl').get('bitArray'))
    var.put('h', var.get('g').get('i'))
    var.put('e', Js(8.0), '/')
    if (((var.get('e')%Js(2.0)) or (Js(4.0)>var.get('e'))) or (Js(16.0)<var.get('e'))):
        PyJsTempException = JsToPyException(var.get('sjcl').get('exception').get('invalid').create(Js('ccm: invalid tag length')))
        raise PyJsTempException
    if ((Js(4294967295)<var.get('d').get('length')) or (Js(4294967295)<var.get('b').get('length'))):
        PyJsTempException = JsToPyException(var.get('sjcl').get('exception').get('bug').create(Js("ccm: can't deal with 4GiB or more data")))
        raise PyJsTempException
    var.put('c', var.get('sjcl').get('mode').get('ccm').callprop('na', var.get('a'), var.get('d'), var.get('c'), var.get('e'), (var.get('g').callprop('bitLength', var.get('b'))/Js(8.0)), var.get('f')))
    #for JS loop
    var.put('d', Js(0.0))
    while (var.get('d')<var.get('b').get('length')):
        try:
            var.put('c', var.get('a').callprop('encrypt', var.get('h')(var.get('c'), var.get('b').callprop('slice', var.get('d'), (var.get('d')+Js(4.0))).callprop('concat', Js([Js(0.0), Js(0.0), Js(0.0)])))))
        finally:
                var.put('d', Js(4.0), '+')
    return var.get('g').callprop('clamp', var.get('c'), (Js(8.0)*var.get('e')))
PyJs_anonymous_75_._set_name('anonymous')
@Js
def PyJs_anonymous_76_(a, b, c, d, e, f, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'e':e, 'f':f, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'h', 'k', 'l', 'f', 'g', 'b', 'c', 'a', 'n', 'm', 'd'])
    var.put('h', var.get('sjcl').get('bitArray'))
    var.put('g', var.get('h').get('i'))
    var.put('k', var.get('b').get('length'))
    var.put('l', var.get('h').callprop('bitLength', var.get('b')))
    var.put('n', (var.get('k')/Js(50.0)))
    var.put('m', var.get('n'))
    var.put('c', var.get('h').callprop('concat', Js([var.get('h').callprop('partial', Js(8.0), (var.get('f')-Js(1.0)))]), var.get('c')).callprop('concat', Js([Js(0.0), Js(0.0), Js(0.0)])).callprop('slice', Js(0.0), Js(4.0)))
    var.put('d', var.get('h').callprop('bitSlice', var.get('g')(var.get('d'), var.get('a').callprop('encrypt', var.get('c'))), Js(0.0), var.get('e')))
    if var.get('k').neg():
        PyJs_Object_77_ = Js({'tag':var.get('d'),'data':Js([])})
        return PyJs_Object_77_
    #for JS loop
    var.put('g', Js(0.0))
    while (var.get('g')<var.get('k')):
        try:
            def PyJs_LONG_78_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma(((var.get('g')>var.get('n')) and PyJsComma(var.get('sjcl').get('mode').get('ccm').callprop('fa', (var.get('g')/var.get('k'))),var.put('n', var.get('m'), '+'))),(var.get('c').put('3',Js(var.get('c').get('3').to_number())+Js(1))-Js(1))),var.put('e', var.get('a').callprop('encrypt', var.get('c')))),var.get('b').put(var.get('g'), var.get('e').get('0'), '^')),var.get('b').put((var.get('g')+Js(1.0)), var.get('e').get('1'), '^')),var.get('b').put((var.get('g')+Js(2.0)), var.get('e').get('2'), '^')),var.get('b').put((var.get('g')+Js(3.0)), var.get('e').get('3'), '^'))
            PyJs_LONG_78_()
        finally:
                var.put('g', Js(4.0), '+')
    PyJs_Object_79_ = Js({'tag':var.get('d'),'data':var.get('h').callprop('clamp', var.get('b'), var.get('l'))})
    return PyJs_Object_79_
PyJs_anonymous_76_._set_name('anonymous')
PyJs_Object_67_ = Js({'name':Js('ccm'),'G':Js([]),'listenProgress':PyJs_anonymous_68_,'unListenProgress':PyJs_anonymous_69_,'fa':PyJs_anonymous_70_,'encrypt':PyJs_anonymous_71_,'decrypt':PyJs_anonymous_72_,'na':PyJs_anonymous_73_,'V':PyJs_anonymous_75_,'C':PyJs_anonymous_76_})
var.get('sjcl').get('mode').put('ccm', PyJs_Object_67_)
@Js
def PyJs_anonymous_81_(a, b, c, d, e, f, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'e':e, 'f':f, 'this':this, 'arguments':arguments}, var)
    var.registers(['p', 'e', 'h', 'k', 'l', 'f', 'g', 'b', 'c', 'a', 'n', 'm', 'd'])
    if PyJsStrictNeq(Js(128.0),var.get('sjcl').get('bitArray').callprop('bitLength', var.get('c'))):
        PyJsTempException = JsToPyException(var.get('sjcl').get('exception').get('invalid').create(Js('ocb iv must be 128 bits')))
        raise PyJsTempException
    var.put('h', var.get('sjcl').get('mode').get('ocb2').get('S'))
    var.put('k', var.get('sjcl').get('bitArray'))
    var.put('l', var.get('k').get('i'))
    var.put('n', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    var.put('c', var.get('h')(var.get('a').callprop('encrypt', var.get('c'))))
    var.put('p', Js([]))
    var.put('d', (var.get('d') or Js([])))
    var.put('e', (var.get('e') or Js(64.0)))
    #for JS loop
    var.put('g', Js(0.0))
    while ((var.get('g')+Js(4.0))<var.get('b').get('length')):
        try:
            PyJsComma(PyJsComma(PyJsComma(var.put('m', var.get('b').callprop('slice', var.get('g'), (var.get('g')+Js(4.0)))),var.put('n', var.get('l')(var.get('n'), var.get('m')))),var.put('p', var.get('p').callprop('concat', var.get('l')(var.get('c'), var.get('a').callprop('encrypt', var.get('l')(var.get('c'), var.get('m'))))))),var.put('c', var.get('h')(var.get('c'))))
        finally:
                var.put('g', Js(4.0), '+')
    var.put('m', var.get('b').callprop('slice', var.get('g')))
    var.put('b', var.get('k').callprop('bitLength', var.get('m')))
    var.put('g', var.get('a').callprop('encrypt', var.get('l')(var.get('c'), Js([Js(0.0), Js(0.0), Js(0.0), var.get('b')]))))
    var.put('m', var.get('k').callprop('clamp', var.get('l')(var.get('m').callprop('concat', Js([Js(0.0), Js(0.0), Js(0.0)])), var.get('g')), var.get('b')))
    var.put('n', var.get('l')(var.get('n'), var.get('l')(var.get('m').callprop('concat', Js([Js(0.0), Js(0.0), Js(0.0)])), var.get('g'))))
    var.put('n', var.get('a').callprop('encrypt', var.get('l')(var.get('n'), var.get('l')(var.get('c'), var.get('h')(var.get('c'))))))
    (var.get('d').get('length') and var.put('n', var.get('l')(var.get('n'), (var.get('d') if var.get('f') else var.get('sjcl').get('mode').get('ocb2').callprop('pmac', var.get('a'), var.get('d'))))))
    return var.get('p').callprop('concat', var.get('k').callprop('concat', var.get('m'), var.get('k').callprop('clamp', var.get('n'), var.get('e'))))
PyJs_anonymous_81_._set_name('anonymous')
@Js
def PyJs_anonymous_82_(a, b, c, d, e, f, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'e':e, 'f':f, 'this':this, 'arguments':arguments}, var)
    var.registers(['p', 'q', 'e', 'h', 'k', 'l', 'f', 'g', 'b', 'c', 'a', 'r', 'n', 'm', 'd'])
    if PyJsStrictNeq(Js(128.0),var.get('sjcl').get('bitArray').callprop('bitLength', var.get('c'))):
        PyJsTempException = JsToPyException(var.get('sjcl').get('exception').get('invalid').create(Js('ocb iv must be 128 bits')))
        raise PyJsTempException
    var.put('e', (var.get('e') or Js(64.0)))
    var.put('g', var.get('sjcl').get('mode').get('ocb2').get('S'))
    var.put('h', var.get('sjcl').get('bitArray'))
    var.put('k', var.get('h').get('i'))
    var.put('l', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    var.put('n', var.get('g')(var.get('a').callprop('encrypt', var.get('c'))))
    var.put('r', (var.get('sjcl').get('bitArray').callprop('bitLength', var.get('b'))-var.get('e')))
    var.put('q', Js([]))
    var.put('d', (var.get('d') or Js([])))
    #for JS loop
    var.put('c', Js(0.0))
    while ((var.get('c')+Js(4.0))<(var.get('r')/Js(32.0))):
        try:
            PyJsComma(PyJsComma(PyJsComma(var.put('m', var.get('k')(var.get('n'), var.get('a').callprop('decrypt', var.get('k')(var.get('n'), var.get('b').callprop('slice', var.get('c'), (var.get('c')+Js(4.0))))))),var.put('l', var.get('k')(var.get('l'), var.get('m')))),var.put('q', var.get('q').callprop('concat', var.get('m')))),var.put('n', var.get('g')(var.get('n'))))
        finally:
                var.put('c', Js(4.0), '+')
    var.put('p', (var.get('r')-(Js(32.0)*var.get('c'))))
    var.put('m', var.get('a').callprop('encrypt', var.get('k')(var.get('n'), Js([Js(0.0), Js(0.0), Js(0.0), var.get('p')]))))
    var.put('m', var.get('k')(var.get('m'), var.get('h').callprop('clamp', var.get('b').callprop('slice', var.get('c')), var.get('p')).callprop('concat', Js([Js(0.0), Js(0.0), Js(0.0)]))))
    var.put('l', var.get('k')(var.get('l'), var.get('m')))
    var.put('l', var.get('a').callprop('encrypt', var.get('k')(var.get('l'), var.get('k')(var.get('n'), var.get('g')(var.get('n'))))))
    (var.get('d').get('length') and var.put('l', var.get('k')(var.get('l'), (var.get('d') if var.get('f') else var.get('sjcl').get('mode').get('ocb2').callprop('pmac', var.get('a'), var.get('d'))))))
    if var.get('h').callprop('equal', var.get('h').callprop('clamp', var.get('l'), var.get('e')), var.get('h').callprop('bitSlice', var.get('b'), var.get('r'))).neg():
        PyJsTempException = JsToPyException(var.get('sjcl').get('exception').get('corrupt').create(Js("ocb: tag doesn't match")))
        raise PyJsTempException
    return var.get('q').callprop('concat', var.get('h').callprop('clamp', var.get('m'), var.get('p')))
PyJs_anonymous_82_._set_name('anonymous')
@Js
def PyJs_anonymous_83_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'h', 'f', 'g', 'b', 'c', 'a', 'd'])
    var.put('d', var.get('sjcl').get('mode').get('ocb2').get('S'))
    var.put('e', var.get('sjcl').get('bitArray'))
    var.put('f', var.get('e').get('i'))
    var.put('g', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    var.put('h', var.get('a').callprop('encrypt', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0)])))
    var.put('h', var.get('f')(var.get('h'), var.get('d')(var.get('d')(var.get('h')))))
    #for JS loop
    var.put('c', Js(0.0))
    while ((var.get('c')+Js(4.0))<var.get('b').get('length')):
        try:
            PyJsComma(var.put('h', var.get('d')(var.get('h'))),var.put('g', var.get('f')(var.get('g'), var.get('a').callprop('encrypt', var.get('f')(var.get('h'), var.get('b').callprop('slice', var.get('c'), (var.get('c')+Js(4.0))))))))
        finally:
                var.put('c', Js(4.0), '+')
    var.put('c', var.get('b').callprop('slice', var.get('c')))
    ((Js(128.0)>var.get('e').callprop('bitLength', var.get('c'))) and PyJsComma(var.put('h', var.get('f')(var.get('h'), var.get('d')(var.get('h')))),var.put('c', var.get('e').callprop('concat', var.get('c'), Js([(-Js(2147483648.0)), Js(0.0), Js(0.0), Js(0.0)])))))
    var.put('g', var.get('f')(var.get('g'), var.get('c')))
    return var.get('a').callprop('encrypt', var.get('f')(var.get('d')(var.get('f')(var.get('h'), var.get('d')(var.get('h')))), var.get('g')))
PyJs_anonymous_83_._set_name('anonymous')
@Js
def PyJs_anonymous_84_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    return Js([((var.get('a').get('0')<<Js(1.0))^PyJsBshift(var.get('a').get('1'),Js(31.0))), ((var.get('a').get('1')<<Js(1.0))^PyJsBshift(var.get('a').get('2'),Js(31.0))), ((var.get('a').get('2')<<Js(1.0))^PyJsBshift(var.get('a').get('3'),Js(31.0))), ((var.get('a').get('3')<<Js(1.0))^(Js(135.0)*PyJsBshift(var.get('a').get('0'),Js(31.0))))])
PyJs_anonymous_84_._set_name('anonymous')
PyJs_Object_80_ = Js({'name':Js('ocb2'),'encrypt':PyJs_anonymous_81_,'decrypt':PyJs_anonymous_82_,'pmac':PyJs_anonymous_83_,'S':PyJs_anonymous_84_})
var.get('sjcl').get('mode').put('ocb2', PyJs_Object_80_)
@Js
def PyJs_anonymous_86_(a, b, c, d, e, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'f', 'b', 'c', 'a', 'd'])
    var.put('f', var.get('b').callprop('slice', Js(0.0)))
    var.put('b', var.get('sjcl').get('bitArray'))
    var.put('d', (var.get('d') or Js([])))
    var.put('a', var.get('sjcl').get('mode').get('gcm').callprop('C', Js(0.0).neg(), var.get('a'), var.get('f'), var.get('d'), var.get('c'), (var.get('e') or Js(128.0))))
    return var.get('b').callprop('concat', var.get('a').get('data'), var.get('a').get('tag'))
PyJs_anonymous_86_._set_name('anonymous')
@Js
def PyJs_anonymous_87_(a, b, c, d, e, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'h', 'f', 'g', 'b', 'c', 'a', 'd'])
    var.put('f', var.get('b').callprop('slice', Js(0.0)))
    var.put('g', var.get('sjcl').get('bitArray'))
    var.put('h', var.get('g').callprop('bitLength', var.get('f')))
    var.put('e', (var.get('e') or Js(128.0)))
    var.put('d', (var.get('d') or Js([])))
    (PyJsComma(var.put('b', var.get('g').callprop('bitSlice', var.get('f'), (var.get('h')-var.get('e')))),var.put('f', var.get('g').callprop('bitSlice', var.get('f'), Js(0.0), (var.get('h')-var.get('e'))))) if (var.get('e')<=var.get('h')) else PyJsComma(var.put('b', var.get('f')),var.put('f', Js([]))))
    var.put('a', var.get('sjcl').get('mode').get('gcm').callprop('C', Js(1.0).neg(), var.get('a'), var.get('f'), var.get('d'), var.get('c'), var.get('e')))
    if var.get('g').callprop('equal', var.get('a').get('tag'), var.get('b')).neg():
        PyJsTempException = JsToPyException(var.get('sjcl').get('exception').get('corrupt').create(Js("gcm: tag doesn't match")))
        raise PyJsTempException
    return var.get('a').get('data')
PyJs_anonymous_87_._set_name('anonymous')
@Js
def PyJs_anonymous_88_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'h', 'f', 'g', 'b', 'c', 'a', 'd'])
    var.put('h', var.get('sjcl').get('bitArray').get('i'))
    var.put('e', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    var.put('f', var.get('b').callprop('slice', Js(0.0)))
    #for JS loop
    var.put('c', Js(0.0))
    while (Js(128.0)>var.get('c')):
        try:
            (var.put('d', PyJsStrictNeq(Js(0.0),(var.get('a').get(var.get('Math').callprop('floor', (var.get('c')/Js(32.0))))&(Js(1.0)<<(Js(31.0)-(var.get('c')%Js(32.0))))))) and var.put('e', var.get('h')(var.get('e'), var.get('f'))))
            var.put('g', PyJsStrictNeq(Js(0.0),(var.get('f').get('3')&Js(1.0))))
            #for JS loop
            var.put('d', Js(3.0))
            while (Js(0.0)<var.get('d')):
                try:
                    var.get('f').put(var.get('d'), (PyJsBshift(var.get('f').get(var.get('d')),Js(1.0))|((var.get('f').get((var.get('d')-Js(1.0)))&Js(1.0))<<Js(31.0))))
                finally:
                        (var.put('d',Js(var.get('d').to_number())-Js(1))+Js(1))
            var.get('f').put('0', Js(1.0), '>>>')
            (var.get('g') and var.get('f').put('0', (-Js(520093696)), '^'))
        finally:
                (var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1))
    return var.get('e')
PyJs_anonymous_88_._set_name('anonymous')
@Js
def PyJs_anonymous_89_(a, b, c, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'b', 'c', 'a', 'd'])
    var.put('e', var.get('c').get('length'))
    var.put('b', var.get('b').callprop('slice', Js(0.0)))
    #for JS loop
    var.put('d', Js(0.0))
    while (var.get('d')<var.get('e')):
        try:
            def PyJs_LONG_90_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('b').put('0', (Js(4294967295)&var.get('c').get(var.get('d'))), '^'),var.get('b').put('1', (Js(4294967295)&var.get('c').get((var.get('d')+Js(1.0)))), '^')),var.get('b').put('2', (Js(4294967295)&var.get('c').get((var.get('d')+Js(2.0)))), '^')),var.get('b').put('3', (Js(4294967295)&var.get('c').get((var.get('d')+Js(3.0)))), '^')),var.put('b', var.get('sjcl').get('mode').get('gcm').callprop('ka', var.get('b'), var.get('a'))))
            PyJs_LONG_90_()
        finally:
                var.put('d', Js(4.0), '+')
    return var.get('b')
PyJs_anonymous_89_._set_name('anonymous')
@Js
def PyJs_anonymous_91_(a, b, c, d, e, f, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'e':e, 'f':f, 'this':this, 'arguments':arguments}, var)
    var.registers(['p', 'q', 'e', 'h', 'k', 'l', 'f', 'g', 'b', 'c', 'a', 'r', 'n', 'm', 'd'])
    var.put('q', var.get('sjcl').get('bitArray'))
    var.put('m', var.get('c').get('length'))
    var.put('p', var.get('q').callprop('bitLength', var.get('c')))
    var.put('r', var.get('q').callprop('bitLength', var.get('d')))
    var.put('h', var.get('q').callprop('bitLength', var.get('e')))
    var.put('g', var.get('b').callprop('encrypt', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0)])))
    def PyJs_LONG_92_(var=var):
        return (PyJsComma(var.put('e', var.get('e').callprop('slice', Js(0.0))),var.put('e', var.get('q').callprop('concat', var.get('e'), Js([Js(1.0)])))) if PyJsStrictEq(Js(96.0),var.get('h')) else PyJsComma(var.put('e', var.get('sjcl').get('mode').get('gcm').callprop('j', var.get('g'), Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0)]), var.get('e'))),var.put('e', var.get('sjcl').get('mode').get('gcm').callprop('j', var.get('g'), var.get('e'), Js([Js(0.0), Js(0.0), var.get('Math').callprop('floor', (var.get('h')/Js(4294967296))), (var.get('h')&Js(4294967295))])))))
    PyJs_LONG_92_()
    var.put('h', var.get('sjcl').get('mode').get('gcm').callprop('j', var.get('g'), Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0)]), var.get('d')))
    var.put('n', var.get('e').callprop('slice', Js(0.0)))
    var.put('d', var.get('h').callprop('slice', Js(0.0)))
    (var.get('a') or var.put('d', var.get('sjcl').get('mode').get('gcm').callprop('j', var.get('g'), var.get('h'), var.get('c'))))
    #for JS loop
    var.put('l', Js(0.0))
    while (var.get('l')<var.get('m')):
        try:
            def PyJs_LONG_93_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(PyJsComma((var.get('n').put('3',Js(var.get('n').get('3').to_number())+Js(1))-Js(1)),var.put('k', var.get('b').callprop('encrypt', var.get('n')))),var.get('c').put(var.get('l'), var.get('k').get('0'), '^')),var.get('c').put((var.get('l')+Js(1.0)), var.get('k').get('1'), '^')),var.get('c').put((var.get('l')+Js(2.0)), var.get('k').get('2'), '^')),var.get('c').put((var.get('l')+Js(3.0)), var.get('k').get('3'), '^'))
            PyJs_LONG_93_()
        finally:
                var.put('l', Js(4.0), '+')
    var.put('c', var.get('q').callprop('clamp', var.get('c'), var.get('p')))
    (var.get('a') and var.put('d', var.get('sjcl').get('mode').get('gcm').callprop('j', var.get('g'), var.get('h'), var.get('c'))))
    var.put('a', Js([var.get('Math').callprop('floor', (var.get('r')/Js(4294967296))), (var.get('r')&Js(4294967295)), var.get('Math').callprop('floor', (var.get('p')/Js(4294967296))), (var.get('p')&Js(4294967295))]))
    var.put('d', var.get('sjcl').get('mode').get('gcm').callprop('j', var.get('g'), var.get('d'), var.get('a')))
    var.put('k', var.get('b').callprop('encrypt', var.get('e')))
    var.get('d').put('0', var.get('k').get('0'), '^')
    var.get('d').put('1', var.get('k').get('1'), '^')
    var.get('d').put('2', var.get('k').get('2'), '^')
    var.get('d').put('3', var.get('k').get('3'), '^')
    PyJs_Object_94_ = Js({'tag':var.get('q').callprop('bitSlice', var.get('d'), Js(0.0), var.get('f')),'data':var.get('c')})
    return PyJs_Object_94_
PyJs_anonymous_91_._set_name('anonymous')
PyJs_Object_85_ = Js({'name':Js('gcm'),'encrypt':PyJs_anonymous_86_,'decrypt':PyJs_anonymous_87_,'ka':PyJs_anonymous_88_,'j':PyJs_anonymous_89_,'C':PyJs_anonymous_91_})
var.get('sjcl').get('mode').put('gcm', PyJs_Object_85_)
@Js
def PyJs_anonymous_95_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'b', 'c', 'a', 'd'])
    var.get(u"this").put('W', var.put('b', (var.get('b') or var.get('sjcl').get('hash').get('sha256'))))
    var.put('c', Js([Js([]), Js([])]))
    var.put('e', (var.get('b').get('prototype').get('blockSize')/Js(32.0)))
    var.get(u"this").put('w', Js([var.get('b').create(), var.get('b').create()]))
    ((var.get('a').get('length')>var.get('e')) and var.put('a', var.get('b').callprop('hash', var.get('a'))))
    #for JS loop
    var.put('d', Js(0.0))
    while (var.get('d')<var.get('e')):
        try:
            PyJsComma(var.get('c').get('0').put(var.get('d'), (var.get('a').get(var.get('d'))^Js(909522486.0))),var.get('c').get('1').put(var.get('d'), (var.get('a').get(var.get('d'))^Js(1549556828.0))))
        finally:
                (var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1))
    var.get(u"this").get('w').get('0').callprop('update', var.get('c').get('0'))
    var.get(u"this").get('w').get('1').callprop('update', var.get('c').get('1'))
    var.get(u"this").put('R', var.get('b').create(var.get(u"this").get('w').get('0')))
PyJs_anonymous_95_._set_name('anonymous')
var.get('sjcl').get('misc').put('hmac', PyJs_anonymous_95_)
@Js
def PyJs_anonymous_96_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    if var.get(u"this").get('aa'):
        PyJsTempException = JsToPyException(var.get('sjcl').get('exception').get('invalid').create(Js('encrypt on already updated hmac called!')))
        raise PyJsTempException
    var.get(u"this").callprop('update', var.get('a'))
    return var.get(u"this").callprop('digest', var.get('a'))
PyJs_anonymous_96_._set_name('anonymous')
var.get('sjcl').get('misc').get('hmac').get('prototype').put('encrypt', var.get('sjcl').get('misc').get('hmac').get('prototype').put('mac', PyJs_anonymous_96_))
@Js
def PyJs_anonymous_97_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    var.get(u"this").put('R', var.get(u"this").get('W').create(var.get(u"this").get('w').get('0')))
    var.get(u"this").put('aa', Js(1.0).neg())
PyJs_anonymous_97_._set_name('anonymous')
var.get('sjcl').get('misc').get('hmac').get('prototype').put('reset', PyJs_anonymous_97_)
@Js
def PyJs_anonymous_98_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    var.get(u"this").put('aa', Js(0.0).neg())
    var.get(u"this").get('R').callprop('update', var.get('a'))
PyJs_anonymous_98_._set_name('anonymous')
var.get('sjcl').get('misc').get('hmac').get('prototype').put('update', PyJs_anonymous_98_)
@Js
def PyJs_anonymous_99_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    var.put('a', var.get(u"this").get('R').callprop('finalize'))
    var.put('a', var.get(u"this").get('W').create(var.get(u"this").get('w').get('1')).callprop('update', var.get('a')).callprop('finalize'))
    var.get(u"this").callprop('reset')
    return var.get('a')
PyJs_anonymous_99_._set_name('anonymous')
var.get('sjcl').get('misc').get('hmac').get('prototype').put('digest', PyJs_anonymous_99_)
@Js
def PyJs_anonymous_100_(a, b, c, d, e, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'h', 'k', 'l', 'f', 'g', 'b', 'c', 'a', 'n', 'd'])
    var.put('c', (var.get('c') or Js(10000.0)))
    if ((Js(0.0)>var.get('d')) or (Js(0.0)>var.get('c'))):
        PyJsTempException = JsToPyException(var.get('sjcl').get('exception').get('invalid').create(Js('invalid params to pbkdf2')))
        raise PyJsTempException
    (PyJsStrictEq(Js('string'),var.get('a',throw=False).typeof()) and var.put('a', var.get('sjcl').get('codec').get('utf8String').callprop('toBits', var.get('a'))))
    (PyJsStrictEq(Js('string'),var.get('b',throw=False).typeof()) and var.put('b', var.get('sjcl').get('codec').get('utf8String').callprop('toBits', var.get('b'))))
    var.put('e', (var.get('e') or var.get('sjcl').get('misc').get('hmac')))
    var.put('a', var.get('e').create(var.get('a')))
    var.put('l', Js([]))
    var.put('n', var.get('sjcl').get('bitArray'))
    #for JS loop
    var.put('k', Js(1.0))
    while ((Js(32.0)*var.get('l').get('length'))<(var.get('d') or Js(1.0))):
        try:
            var.put('e', var.put('f', var.get('a').callprop('encrypt', var.get('n').callprop('concat', var.get('b'), Js([var.get('k')])))))
            #for JS loop
            var.put('g', Js(1.0))
            while (var.get('g')<var.get('c')):
                try:
                    #for JS loop
                    PyJsComma(var.put('f', var.get('a').callprop('encrypt', var.get('f'))),var.put('h', Js(0.0)))
                    while (var.get('h')<var.get('f').get('length')):
                        try:
                            var.get('e').put(var.get('h'), var.get('f').get(var.get('h')), '^')
                        finally:
                                (var.put('h',Js(var.get('h').to_number())+Js(1))-Js(1))
                finally:
                        (var.put('g',Js(var.get('g').to_number())+Js(1))-Js(1))
            var.put('l', var.get('l').callprop('concat', var.get('e')))
        finally:
                (var.put('k',Js(var.get('k').to_number())+Js(1))-Js(1))
    (var.get('d') and var.put('l', var.get('n').callprop('clamp', var.get('l'), var.get('d'))))
    return var.get('l')
PyJs_anonymous_100_._set_name('anonymous')
var.get('sjcl').get('misc').put('pbkdf2', PyJs_anonymous_100_)
@Js
def PyJs_anonymous_101_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    var.get(u"this").put('c', Js([var.get('sjcl').get('hash').get('sha256').create()]))
    var.get(u"this").put('m', Js([Js(0.0)]))
    var.get(u"this").put('P', Js(0.0))
    PyJs_Object_102_ = Js({})
    var.get(u"this").put('H', PyJs_Object_102_)
    var.get(u"this").put('N', Js(0.0))
    PyJs_Object_103_ = Js({})
    var.get(u"this").put('U', PyJs_Object_103_)
    var.get(u"this").put('Z', var.get(u"this").put('f', var.get(u"this").put('o', var.get(u"this").put('ha', Js(0.0)))))
    var.get(u"this").put('b', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    var.get(u"this").put('h', Js([Js(0.0), Js(0.0), Js(0.0), Js(0.0)]))
    var.get(u"this").put('L', PyJsComma(Js(0.0), Js(None)))
    var.get(u"this").put('M', var.get('a'))
    var.get(u"this").put('D', Js(1.0).neg())
    PyJs_Object_105_ = Js({})
    PyJs_Object_106_ = Js({})
    PyJs_Object_104_ = Js({'progress':PyJs_Object_105_,'seeded':PyJs_Object_106_})
    var.get(u"this").put('K', PyJs_Object_104_)
    var.get(u"this").put('u', var.get(u"this").put('ga', Js(0.0)))
    var.get(u"this").put('I', Js(1.0))
    var.get(u"this").put('J', Js(2.0))
    var.get(u"this").put('ca', Js(65536))
    var.get(u"this").put('T', Js([Js(0.0), Js(48.0), Js(64.0), Js(96.0), Js(128.0), Js(192.0), Js(256), Js(384.0), Js(512.0), Js(768.0), Js(1024.0)]))
    var.get(u"this").put('da', Js(30000.0))
    var.get(u"this").put('ba', Js(80.0))
PyJs_anonymous_101_._set_name('anonymous')
var.get('sjcl').put('prng', PyJs_anonymous_101_)
@Js
def PyJs_anonymous_108_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'f', 'g', 'b', 'c', 'a', 'd'])
    var.put('c', Js([]))
    var.put('d', var.get(u"this").callprop('isReady', var.get('b')))
    pass
    if PyJsStrictEq(var.get('d'),var.get(u"this").get('u')):
        PyJsTempException = JsToPyException(var.get('sjcl').get('exception').get('notReady').create(Js("generator isn't seeded")))
        raise PyJsTempException
    if (var.get('d')&var.get(u"this").get('J')):
        var.put('d', (var.get('d')&var.get(u"this").get('I')).neg())
        var.put('e', Js([]))
        var.put('f', Js(0.0))
        var.get(u"this").put('Z', var.get('e').put('0', (var.get('Date').create().callprop('valueOf')+var.get(u"this").get('da'))))
        #for JS loop
        var.put('g', Js(0.0))
        while (Js(16.0)>var.get('g')):
            try:
                var.get('e').callprop('push', ((Js(4294967296)*var.get('Math').callprop('random'))|Js(0.0)))
            finally:
                    (var.put('g',Js(var.get('g').to_number())+Js(1))-Js(1))
        #for JS loop
        var.put('g', Js(0.0))
        while ((var.get('g')<var.get(u"this").get('c').get('length')) and PyJsComma(PyJsComma(PyJsComma(var.put('e', var.get('e').callprop('concat', var.get(u"this").get('c').get(var.get('g')).callprop('finalize'))),var.put('f', var.get(u"this").get('m').get(var.get('g')), '+')),var.get(u"this").get('m').put(var.get('g'), Js(0.0))),(var.get('d') or (var.get(u"this").get('P')&(Js(1.0)<<var.get('g'))).neg()))):
            try:
                pass
            finally:
                    (var.put('g',Js(var.get('g').to_number())+Js(1))-Js(1))
        ((var.get(u"this").get('P')>=(Js(1.0)<<var.get(u"this").get('c').get('length'))) and PyJsComma(var.get(u"this").get('c').callprop('push', var.get('sjcl').get('hash').get('sha256').create()),var.get(u"this").get('m').callprop('push', Js(0.0))))
        var.get(u"this").put('f', var.get('f'), '-')
        ((var.get('f')>var.get(u"this").get('o')) and var.get(u"this").put('o', var.get('f')))
        (var.get(u"this").put('P',Js(var.get(u"this").get('P').to_number())+Js(1))-Js(1))
        var.get(u"this").put('b', var.get('sjcl').get('hash').get('sha256').callprop('hash', var.get(u"this").get('b').callprop('concat', var.get('e'))))
        var.get(u"this").put('L', var.get('sjcl').get('cipher').get('aes').create(var.get(u"this").get('b')))
        #for JS loop
        var.put('d', Js(0.0))
        while ((Js(4.0)>var.get('d')) and PyJsComma(var.get(u"this").get('h').put(var.get('d'), ((var.get(u"this").get('h').get(var.get('d'))+Js(1.0))|Js(0.0))),var.get(u"this").get('h').get(var.get('d')).neg())):
            try:
                pass
            finally:
                    (var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1))
    #for JS loop
    var.put('d', Js(0.0))
    while (var.get('d')<var.get('a')):
        try:
            PyJsComma(PyJsComma((PyJsStrictEq(Js(0.0),((var.get('d')+Js(1.0))%var.get(u"this").get('ca'))) and var.get('y')(var.get(u"this"))),var.put('e', var.get('z')(var.get(u"this")))),var.get('c').callprop('push', var.get('e').get('0'), var.get('e').get('1'), var.get('e').get('2'), var.get('e').get('3')))
        finally:
                var.put('d', Js(4.0), '+')
    var.get('y')(var.get(u"this"))
    return var.get('c').callprop('slice', Js(0.0), var.get('a'))
PyJs_anonymous_108_._set_name('anonymous')
@Js
def PyJs_anonymous_109_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', 'b'])
    if (PyJsStrictEq(Js(0.0),var.get('a')) and PyJsStrictNeq(Js('Setting paranoia=0 will ruin your security; use it only for testing'),var.get('b'))):
        PyJsTempException = JsToPyException(var.get('sjcl').get('exception').get('invalid').create(Js('Setting paranoia=0 will ruin your security; use it only for testing')))
        raise PyJsTempException
    var.get(u"this").put('M', var.get('a'))
PyJs_anonymous_109_._set_name('anonymous')
@Js
def PyJs_anonymous_110_(a, b, c, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'h', 'k', 'f', 'g', 'b', 'c', 'a', 'd'])
    var.put('c', (var.get('c') or Js('user')))
    var.put('f', var.get('Date').create().callprop('valueOf'))
    var.put('g', var.get(u"this").get('H').get(var.get('c')))
    var.put('h', var.get(u"this").callprop('isReady'))
    var.put('k', Js(0.0))
    var.put('d', var.get(u"this").get('U').get(var.get('c')))
    (PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get('d')) and var.put('d', var.get(u"this").get('U').put(var.get('c'), (var.get(u"this").put('ha',Js(var.get(u"this").get('ha').to_number())+Js(1))-Js(1)))))
    (PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get('g')) and var.put('g', var.get(u"this").get('H').put(var.get('c'), Js(0.0))))
    var.get(u"this").get('H').put(var.get('c'), ((var.get(u"this").get('H').get(var.get('c'))+Js(1.0))%var.get(u"this").get('c').get('length')))
    while 1:
        SWITCHED = False
        CONDITION = (var.get('a',throw=False).typeof())
        if SWITCHED or PyJsStrictEq(CONDITION, Js('number')):
            SWITCHED = True
            (PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get('b')) and var.put('b', Js(1.0)))
            var.get(u"this").get('c').get(var.get('g')).callprop('update', Js([var.get('d'), (var.get(u"this").put('N',Js(var.get(u"this").get('N').to_number())+Js(1))-Js(1)), Js(1.0), var.get('b'), var.get('f'), Js(1.0), (var.get('a')|Js(0.0))]))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('object')):
            SWITCHED = True
            var.put('c', var.get('Object').get('prototype').get('toString').callprop('call', var.get('a')))
            if PyJsStrictEq(Js('[object Uint32Array]'),var.get('c')):
                var.put('e', Js([]))
                #for JS loop
                var.put('c', Js(0.0))
                while (var.get('c')<var.get('a').get('length')):
                    try:
                        var.get('e').callprop('push', var.get('a').get(var.get('c')))
                    finally:
                            (var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1))
                var.put('a', var.get('e'))
            else:
                #for JS loop
                PyJsComma((PyJsStrictNeq(Js('[object Array]'),var.get('c')) and var.put('k', Js(1.0))),var.put('c', Js(0.0)))
                while ((var.get('c')<var.get('a').get('length')) and var.get('k').neg()):
                    try:
                        (PyJsStrictNeq(Js('number'),var.get('a').get(var.get('c')).typeof()) and var.put('k', Js(1.0)))
                    finally:
                            (var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1))
            if var.get('k').neg():
                if PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get('b')):
                    #for JS loop
                    var.put('c', var.put('b', Js(0.0)))
                    while (var.get('c')<var.get('a').get('length')):
                        try:
                            #for JS loop
                            var.put('e', var.get('a').get(var.get('c')))
                            while (Js(0.0)<var.get('e')):
                                PyJsComma((var.put('b',Js(var.get('b').to_number())+Js(1))-Js(1)),var.put('e', PyJsBshift(var.get('e'),Js(1.0))))
                            
                        finally:
                                (var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1))
                var.get(u"this").get('c').get(var.get('g')).callprop('update', Js([var.get('d'), (var.get(u"this").put('N',Js(var.get(u"this").get('N').to_number())+Js(1))-Js(1)), Js(2.0), var.get('b'), var.get('f'), var.get('a').get('length')]).callprop('concat', var.get('a')))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js('string')):
            SWITCHED = True
            (PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get('b')) and var.put('b', var.get('a').get('length')))
            var.get(u"this").get('c').get(var.get('g')).callprop('update', Js([var.get('d'), (var.get(u"this").put('N',Js(var.get(u"this").get('N').to_number())+Js(1))-Js(1)), Js(3.0), var.get('b'), var.get('f'), var.get('a').get('length')]))
            var.get(u"this").get('c').get(var.get('g')).callprop('update', var.get('a'))
            break
        if True:
            SWITCHED = True
            var.put('k', Js(1.0))
        SWITCHED = True
        break
    if var.get('k'):
        PyJsTempException = JsToPyException(var.get('sjcl').get('exception').get('bug').create(Js('random: addEntropy only supports number, array of numbers or string')))
        raise PyJsTempException
    var.get(u"this").get('m').put(var.get('g'), var.get('b'), '+')
    var.get(u"this").put('f', var.get('b'), '+')
    (PyJsStrictEq(var.get('h'),var.get(u"this").get('u')) and PyJsComma((PyJsStrictNeq(var.get(u"this").callprop('isReady'),var.get(u"this").get('u')) and var.get('A')(Js('seeded'), var.get('Math').callprop('max', var.get(u"this").get('o'), var.get(u"this").get('f')))),var.get('A')(Js('progress'), var.get(u"this").callprop('getProgress'))))
PyJs_anonymous_110_._set_name('anonymous')
@Js
def PyJs_anonymous_111_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    var.put('a', var.get(u"this").get('T').get((var.get('a') if PyJsStrictNeq(PyJsComma(Js(0.0), Js(None)),var.get('a')) else var.get(u"this").get('M'))))
    def PyJs_LONG_112_(var=var):
        return (((var.get(u"this").get('J')|var.get(u"this").get('I')) if ((var.get(u"this").get('m').get('0')>var.get(u"this").get('ba')) and (var.get('Date').create().callprop('valueOf')>var.get(u"this").get('Z'))) else var.get(u"this").get('I')) if (var.get(u"this").get('o') and (var.get(u"this").get('o')>=var.get('a'))) else ((var.get(u"this").get('J')|var.get(u"this").get('u')) if (var.get(u"this").get('f')>=var.get('a')) else var.get(u"this").get('u')))
    return PyJs_LONG_112_()
PyJs_anonymous_111_._set_name('anonymous')
@Js
def PyJs_anonymous_113_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    var.put('a', var.get(u"this").get('T').get((var.get('a') if var.get('a') else var.get(u"this").get('M'))))
    return (Js(1.0) if (var.get(u"this").get('o')>=var.get('a')) else (Js(1.0) if (var.get(u"this").get('f')>var.get('a')) else (var.get(u"this").get('f')/var.get('a'))))
PyJs_anonymous_113_._set_name('anonymous')
@Js
def PyJs_anonymous_114_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    if var.get(u"this").get('D').neg():
        PyJs_Object_115_ = Js({'loadTimeCollector':var.get('B')(var.get(u"this"), var.get(u"this").get('ma')),'mouseCollector':var.get('B')(var.get(u"this"), var.get(u"this").get('oa')),'keyboardCollector':var.get('B')(var.get(u"this"), var.get(u"this").get('la')),'accelerometerCollector':var.get('B')(var.get(u"this"), var.get(u"this").get('ea')),'touchCollector':var.get('B')(var.get(u"this"), var.get(u"this").get('qa'))})
        var.get(u"this").put('a', PyJs_Object_115_)
        if var.get('window').get('addEventListener'):
            def PyJs_LONG_116_(var=var):
                return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('window').callprop('addEventListener', Js('load'), var.get(u"this").get('a').get('loadTimeCollector'), Js(1.0).neg()),var.get('window').callprop('addEventListener', Js('mousemove'), var.get(u"this").get('a').get('mouseCollector'), Js(1.0).neg())),var.get('window').callprop('addEventListener', Js('keypress'), var.get(u"this").get('a').get('keyboardCollector'), Js(1.0).neg())),var.get('window').callprop('addEventListener', Js('devicemotion'), var.get(u"this").get('a').get('accelerometerCollector'), Js(1.0).neg())),var.get('window').callprop('addEventListener', Js('touchmove'), var.get(u"this").get('a').get('touchCollector'), Js(1.0).neg()))
            PyJs_LONG_116_()
        else:
            if var.get('document').get('attachEvent'):
                PyJsComma(PyJsComma(var.get('document').callprop('attachEvent', Js('onload'), var.get(u"this").get('a').get('loadTimeCollector')),var.get('document').callprop('attachEvent', Js('onmousemove'), var.get(u"this").get('a').get('mouseCollector'))),var.get('document').callprop('attachEvent', Js('keypress'), var.get(u"this").get('a').get('keyboardCollector')))
            else:
                PyJsTempException = JsToPyException(var.get('sjcl').get('exception').get('bug').create(Js("can't attach event")))
                raise PyJsTempException
        var.get(u"this").put('D', Js(0.0).neg())
PyJs_anonymous_114_._set_name('anonymous')
@Js
def PyJs_anonymous_117_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    def PyJs_LONG_119_(var=var):
        def PyJs_LONG_118_(var=var):
            return PyJsComma(PyJsComma(PyJsComma(PyJsComma(var.get('window').callprop('removeEventListener', Js('load'), var.get(u"this").get('a').get('loadTimeCollector'), Js(1.0).neg()),var.get('window').callprop('removeEventListener', Js('mousemove'), var.get(u"this").get('a').get('mouseCollector'), Js(1.0).neg())),var.get('window').callprop('removeEventListener', Js('keypress'), var.get(u"this").get('a').get('keyboardCollector'), Js(1.0).neg())),var.get('window').callprop('removeEventListener', Js('devicemotion'), var.get(u"this").get('a').get('accelerometerCollector'), Js(1.0).neg())),var.get('window').callprop('removeEventListener', Js('touchmove'), var.get(u"this").get('a').get('touchCollector'), Js(1.0).neg()))
        return (PyJs_LONG_118_() if var.get('window').get('removeEventListener') else (var.get('document').get('detachEvent') and PyJsComma(PyJsComma(var.get('document').callprop('detachEvent', Js('onload'), var.get(u"this").get('a').get('loadTimeCollector')),var.get('document').callprop('detachEvent', Js('onmousemove'), var.get(u"this").get('a').get('mouseCollector'))),var.get('document').callprop('detachEvent', Js('keypress'), var.get(u"this").get('a').get('keyboardCollector')))))
    (var.get(u"this").get('D') and PyJsComma(PyJs_LONG_119_(),var.get(u"this").put('D', Js(1.0).neg())))
PyJs_anonymous_117_._set_name('anonymous')
@Js
def PyJs_anonymous_120_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', 'b'])
    var.get(u"this").get('K').get(var.get('a')).put((var.get(u"this").put('ga',Js(var.get(u"this").get('ga').to_number())+Js(1))-Js(1)), var.get('b'))
PyJs_anonymous_120_._set_name('anonymous')
@Js
def PyJs_anonymous_121_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'f', 'b', 'c', 'a', 'd'])
    var.put('e', var.get(u"this").get('K').get(var.get('a')))
    var.put('f', Js([]))
    for PyJsTemp in var.get('e'):
        var.put('d', PyJsTemp)
        ((var.get('e').callprop('hasOwnProperty', var.get('d')) and PyJsStrictEq(var.get('e').get(var.get('d')),var.get('b'))) and var.get('f').callprop('push', var.get('d')))
    #for JS loop
    var.put('c', Js(0.0))
    while (var.get('c')<var.get('f').get('length')):
        try:
            PyJsComma(var.put('d', var.get('f').get(var.get('c'))),var.get('e').delete(var.get('d')))
        finally:
                (var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1))
PyJs_anonymous_121_._set_name('anonymous')
@Js
def PyJs_anonymous_122_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    var.get('C')(var.get(u"this"), Js(1.0))
PyJs_anonymous_122_._set_name('anonymous')
@Js
def PyJs_anonymous_123_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['c', 'a', 'b'])
    pass
    try:
        PyJsComma(var.put('b', (((var.get('a').get('x') or var.get('a').get('clientX')) or var.get('a').get('offsetX')) or Js(0.0))),var.put('c', (((var.get('a').get('y') or var.get('a').get('clientY')) or var.get('a').get('offsetY')) or Js(0.0))))
    except PyJsException as PyJsTempException:
        PyJsHolder_64_89147456 = var.own.get('d')
        var.force_own_put('d', PyExceptionToJs(PyJsTempException))
        try:
            var.put('c', var.put('b', Js(0.0)))
        finally:
            if PyJsHolder_64_89147456 is not None:
                var.own['d'] = PyJsHolder_64_89147456
            else:
                del var.own['d']
            del PyJsHolder_64_89147456
    (((Js(0.0)!=var.get('b')) and (Js(0.0)!=var.get('c'))) and var.get(u"this").callprop('addEntropy', Js([var.get('b'), var.get('c')]), Js(2.0), Js('mouse')))
    var.get('C')(var.get(u"this"), Js(0.0))
PyJs_anonymous_123_._set_name('anonymous')
@Js
def PyJs_anonymous_124_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    var.put('a', (var.get('a').get('touches').get('0') or var.get('a').get('changedTouches').get('0')))
    var.get(u"this").callprop('addEntropy', Js([(var.get('a').get('pageX') or var.get('a').get('clientX')), (var.get('a').get('pageY') or var.get('a').get('clientY'))]), Js(1.0), Js('touch'))
    var.get('C')(var.get(u"this"), Js(0.0))
PyJs_anonymous_124_._set_name('anonymous')
@Js
def PyJs_anonymous_125_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    var.get('C')(var.get(u"this"), Js(2.0))
PyJs_anonymous_125_._set_name('anonymous')
@Js
def PyJs_anonymous_126_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', 'b'])
    var.put('a', ((var.get('a').get('accelerationIncludingGravity').get('x') or var.get('a').get('accelerationIncludingGravity').get('y')) or var.get('a').get('accelerationIncludingGravity').get('z')))
    if var.get('window').get('orientation'):
        var.put('b', var.get('window').get('orientation'))
        (PyJsStrictEq(Js('number'),var.get('b',throw=False).typeof()) and var.get(u"this").callprop('addEntropy', var.get('b'), Js(1.0), Js('accelerometer')))
    (var.get('a') and var.get(u"this").callprop('addEntropy', var.get('a'), Js(2.0), Js('accelerometer')))
    var.get('C')(var.get(u"this"), Js(0.0))
PyJs_anonymous_126_._set_name('anonymous')
PyJs_Object_107_ = Js({'randomWords':PyJs_anonymous_108_,'setDefaultParanoia':PyJs_anonymous_109_,'addEntropy':PyJs_anonymous_110_,'isReady':PyJs_anonymous_111_,'getProgress':PyJs_anonymous_113_,'startCollectors':PyJs_anonymous_114_,'stopCollectors':PyJs_anonymous_117_,'addEventListener':PyJs_anonymous_120_,'removeEventListener':PyJs_anonymous_121_,'la':PyJs_anonymous_122_,'oa':PyJs_anonymous_123_,'qa':PyJs_anonymous_124_,'ma':PyJs_anonymous_125_,'ea':PyJs_anonymous_126_})
var.get('sjcl').get('prng').put('prototype', PyJs_Object_107_)
pass
pass
pass
pass
pass
var.get('sjcl').put('random', var.get('sjcl').get('prng').create(Js(6.0)))
class JS_BREAK_LABEL_61(Exception): pass
try:
    try:
        pass
        if var.put('G', (PyJsStrictNeq(Js('undefined'),var.get('module',throw=False).typeof()) and var.get('module').get('exports'))):
            pass
            try:
                var.put('H', var.get('require')(Js('crypto')))
            except PyJsException as PyJsTempException:
                PyJsHolder_61_33373117 = var.own.get('a')
                var.force_own_put('a', PyExceptionToJs(PyJsTempException))
                try:
                    var.put('H', var.get(u"null"))
                finally:
                    if PyJsHolder_61_33373117 is not None:
                        var.own['a'] = PyJsHolder_61_33373117
                    else:
                        del var.own['a']
                    del PyJsHolder_61_33373117
            var.put('G', var.put('E', var.get('H')))
        if (var.get('G') and var.get('E').get('randomBytes')):
            PyJsComma(PyJsComma(var.put('D', var.get('E').callprop('randomBytes', Js(128.0))),var.put('D', var.get('Uint32Array').create(var.get('Uint8Array').create(var.get('D')).get('buffer')))),var.get('sjcl').get('random').callprop('addEntropy', var.get('D'), Js(1024.0), Js("crypto['randomBytes']")))
        else:
            if (PyJsStrictNeq(Js('undefined'),var.get('window',throw=False).typeof()) and PyJsStrictNeq(Js('undefined'),var.get('Uint32Array',throw=False).typeof())):
                var.put('F', var.get('Uint32Array').create(Js(32.0)))
                if (var.get('window').get('crypto') and var.get('window').get('crypto').get('getRandomValues')):
                    var.get('window').get('crypto').callprop('getRandomValues', var.get('F'))
                else:
                    if (var.get('window').get('msCrypto') and var.get('window').get('msCrypto').get('getRandomValues')):
                        var.get('window').get('msCrypto').callprop('getRandomValues', var.get('F'))
                    else:
                        raise JS_BREAK_LABEL_61("Breaked")
                var.get('sjcl').get('random').callprop('addEntropy', var.get('F'), Js(1024.0), Js("crypto['getRandomValues']"))
    except PyJsException as PyJsTempException:
        PyJsHolder_61_52828592 = var.own.get('a')
        var.force_own_put('a', PyExceptionToJs(PyJsTempException))
        try:
            ((PyJsStrictNeq(Js('undefined'),var.get('window',throw=False).typeof()) and var.get('window').get('console')) and PyJsComma(var.get('console').callprop('log', Js('There was an error collecting entropy from the browser:')),var.get('console').callprop('log', var.get('a'))))
        finally:
            if PyJsHolder_61_52828592 is not None:
                var.own['a'] = PyJsHolder_61_52828592
            else:
                del var.own['a']
            del PyJsHolder_61_52828592
except JS_BREAK_LABEL_61:
    pass
PyJs_Object_130_ = Js({'v':Js(1.0),'iter':Js(10000.0),'ks':Js(128.0),'ts':Js(64.0),'mode':Js('ccm'),'adata':Js(''),'cipher':Js('aes')})
@Js
def PyJs_anonymous_131_(a, b, c, d, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'f', 'g', 'b', 'c', 'a', 'd'])
    PyJs_Object_132_ = Js({})
    var.put('c', (var.get('c') or PyJs_Object_132_))
    PyJs_Object_133_ = Js({})
    var.put('d', (var.get('d') or PyJs_Object_133_))
    var.put('e', var.get('sjcl').get('json'))
    PyJs_Object_134_ = Js({'iv':var.get('sjcl').get('random').callprop('randomWords', Js(4.0), Js(0.0))})
    var.put('f', var.get('e').callprop('g', PyJs_Object_134_, var.get('e').get('defaults')))
    var.get('e').callprop('g', var.get('f'), var.get('c'))
    var.put('c', var.get('f').get('adata'))
    (PyJsStrictEq(Js('string'),var.get('f').get('salt').typeof()) and var.get('f').put('salt', var.get('sjcl').get('codec').get('base64').callprop('toBits', var.get('f').get('salt'))))
    (PyJsStrictEq(Js('string'),var.get('f').get('iv').typeof()) and var.get('f').put('iv', var.get('sjcl').get('codec').get('base64').callprop('toBits', var.get('f').get('iv'))))
    def PyJs_LONG_135_(var=var):
        return (((var.get('sjcl').get('mode').get(var.get('f').get('mode')).neg() or var.get('sjcl').get('cipher').get(var.get('f').get('cipher')).neg()) or (PyJsStrictEq(Js('string'),var.get('a',throw=False).typeof()) and (Js(100.0)>=var.get('f').get('iter')))) or ((PyJsStrictNeq(Js(64.0),var.get('f').get('ts')) and PyJsStrictNeq(Js(96.0),var.get('f').get('ts'))) and PyJsStrictNeq(Js(128.0),var.get('f').get('ts'))))
    if (((PyJs_LONG_135_() or ((PyJsStrictNeq(Js(128.0),var.get('f').get('ks')) and PyJsStrictNeq(Js(192.0),var.get('f').get('ks'))) and PyJsStrictNeq(Js(256),var.get('f').get('ks')))) or (Js(2.0)>var.get('f').get('iv').get('length'))) or (Js(4.0)<var.get('f').get('iv').get('length'))):
        PyJsTempException = JsToPyException(var.get('sjcl').get('exception').get('invalid').create(Js('json encrypt: invalid parameters')))
        raise PyJsTempException
    def PyJs_LONG_136_(var=var):
        return (PyJsComma(PyJsComma(var.put('g', var.get('sjcl').get('misc').callprop('cachedPbkdf2', var.get('a'), var.get('f'))),var.put('a', var.get('g').get('key').callprop('slice', Js(0.0), (var.get('f').get('ks')/Js(32.0))))),var.get('f').put('salt', var.get('g').get('salt'))) if PyJsStrictEq(Js('string'),var.get('a',throw=False).typeof()) else ((var.get('sjcl').get('ecc') and var.get('a').instanceof(var.get('sjcl').get('ecc').get('elGamal').get('publicKey'))) and PyJsComma(PyJsComma(var.put('g', var.get('a').callprop('kem')),var.get('f').put('kemtag', var.get('g').get('tag'))),var.put('a', var.get('g').get('key').callprop('slice', Js(0.0), (var.get('f').get('ks')/Js(32.0)))))))
    PyJs_LONG_136_()
    (PyJsStrictEq(Js('string'),var.get('b',throw=False).typeof()) and var.put('b', var.get('sjcl').get('codec').get('utf8String').callprop('toBits', var.get('b'))))
    (PyJsStrictEq(Js('string'),var.get('c',throw=False).typeof()) and var.get('f').put('adata', var.put('c', var.get('sjcl').get('codec').get('utf8String').callprop('toBits', var.get('c')))))
    var.put('g', var.get('sjcl').get('cipher').get(var.get('f').get('cipher')).create(var.get('a')))
    var.get('e').callprop('g', var.get('d'), var.get('f'))
    var.get('d').put('key', var.get('a'))
    def PyJs_LONG_137_(var=var):
        return (var.get('sjcl').get('arrayBuffer').get('ccm').callprop('encrypt', var.get('g'), var.get('b'), var.get('f').get('iv'), var.get('c'), var.get('f').get('ts')) if (((PyJsStrictEq(Js('ccm'),var.get('f').get('mode')) and var.get('sjcl').get('arrayBuffer')) and var.get('sjcl').get('arrayBuffer').get('ccm')) and var.get('b').instanceof(var.get('ArrayBuffer'))) else var.get('sjcl').get('mode').get(var.get('f').get('mode')).callprop('encrypt', var.get('g'), var.get('b'), var.get('f').get('iv'), var.get('c'), var.get('f').get('ts')))
    var.get('f').put('ct', PyJs_LONG_137_())
    return var.get('f')
PyJs_anonymous_131_._set_name('anonymous')
@Js
def PyJs_anonymous_138_(a, b, c, d, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'f', 'b', 'c', 'a', 'd'])
    var.put('e', var.get('sjcl').get('json'))
    var.put('f', var.get('e').get('ja').callprop('apply', var.get('e'), var.get('arguments')))
    return var.get('e').callprop('encode', var.get('f'))
PyJs_anonymous_138_._set_name('anonymous')
@Js
def PyJs_anonymous_139_(a, b, c, d, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'f', 'g', 'b', 'c', 'a', 'd'])
    PyJs_Object_140_ = Js({})
    var.put('c', (var.get('c') or PyJs_Object_140_))
    PyJs_Object_141_ = Js({})
    var.put('d', (var.get('d') or PyJs_Object_141_))
    var.put('e', var.get('sjcl').get('json'))
    PyJs_Object_142_ = Js({})
    var.put('b', var.get('e').callprop('g', var.get('e').callprop('g', var.get('e').callprop('g', PyJs_Object_142_, var.get('e').get('defaults')), var.get('b')), var.get('c'), Js(0.0).neg()))
    pass
    var.put('f', var.get('b').get('adata'))
    (PyJsStrictEq(Js('string'),var.get('b').get('salt').typeof()) and var.get('b').put('salt', var.get('sjcl').get('codec').get('base64').callprop('toBits', var.get('b').get('salt'))))
    (PyJsStrictEq(Js('string'),var.get('b').get('iv').typeof()) and var.get('b').put('iv', var.get('sjcl').get('codec').get('base64').callprop('toBits', var.get('b').get('iv'))))
    def PyJs_LONG_143_(var=var):
        return (((var.get('sjcl').get('mode').get(var.get('b').get('mode')).neg() or var.get('sjcl').get('cipher').get(var.get('b').get('cipher')).neg()) or (PyJsStrictEq(Js('string'),var.get('a',throw=False).typeof()) and (Js(100.0)>=var.get('b').get('iter')))) or ((PyJsStrictNeq(Js(64.0),var.get('b').get('ts')) and PyJsStrictNeq(Js(96.0),var.get('b').get('ts'))) and PyJsStrictNeq(Js(128.0),var.get('b').get('ts'))))
    if ((((PyJs_LONG_143_() or ((PyJsStrictNeq(Js(128.0),var.get('b').get('ks')) and PyJsStrictNeq(Js(192.0),var.get('b').get('ks'))) and PyJsStrictNeq(Js(256),var.get('b').get('ks')))) or var.get('b').get('iv').neg()) or (Js(2.0)>var.get('b').get('iv').get('length'))) or (Js(4.0)<var.get('b').get('iv').get('length'))):
        PyJsTempException = JsToPyException(var.get('sjcl').get('exception').get('invalid').create(Js('json decrypt: invalid parameters')))
        raise PyJsTempException
    def PyJs_LONG_144_(var=var):
        return (PyJsComma(PyJsComma(var.put('g', var.get('sjcl').get('misc').callprop('cachedPbkdf2', var.get('a'), var.get('b'))),var.put('a', var.get('g').get('key').callprop('slice', Js(0.0), (var.get('b').get('ks')/Js(32.0))))),var.get('b').put('salt', var.get('g').get('salt'))) if PyJsStrictEq(Js('string'),var.get('a',throw=False).typeof()) else ((var.get('sjcl').get('ecc') and var.get('a').instanceof(var.get('sjcl').get('ecc').get('elGamal').get('secretKey'))) and var.put('a', var.get('a').callprop('unkem', var.get('sjcl').get('codec').get('base64').callprop('toBits', var.get('b').get('kemtag'))).callprop('slice', Js(0.0), (var.get('b').get('ks')/Js(32.0))))))
    PyJs_LONG_144_()
    (PyJsStrictEq(Js('string'),var.get('f',throw=False).typeof()) and var.put('f', var.get('sjcl').get('codec').get('utf8String').callprop('toBits', var.get('f'))))
    var.put('g', var.get('sjcl').get('cipher').get(var.get('b').get('cipher')).create(var.get('a')))
    def PyJs_LONG_145_(var=var):
        return (var.get('sjcl').get('arrayBuffer').get('ccm').callprop('decrypt', var.get('g'), var.get('b').get('ct'), var.get('b').get('iv'), var.get('b').get('tag'), var.get('f'), var.get('b').get('ts')) if (((PyJsStrictEq(Js('ccm'),var.get('b').get('mode')) and var.get('sjcl').get('arrayBuffer')) and var.get('sjcl').get('arrayBuffer').get('ccm')) and var.get('b').get('ct').instanceof(var.get('ArrayBuffer'))) else var.get('sjcl').get('mode').get(var.get('b').get('mode')).callprop('decrypt', var.get('g'), var.get('b').get('ct'), var.get('b').get('iv'), var.get('f'), var.get('b').get('ts')))
    var.put('f', PyJs_LONG_145_())
    var.get('e').callprop('g', var.get('d'), var.get('b'))
    var.get('d').put('key', var.get('a'))
    return (var.get('f') if PyJsStrictEq(Js(1.0),var.get('c').get('raw')) else var.get('sjcl').get('codec').get('utf8String').callprop('fromBits', var.get('f')))
PyJs_anonymous_139_._set_name('anonymous')
@Js
def PyJs_anonymous_146_(a, b, c, d, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 'b', 'c', 'a', 'd'])
    var.put('e', var.get('sjcl').get('json'))
    return var.get('e').callprop('ia', var.get('a'), var.get('e').callprop('decode', var.get('b')), var.get('c'), var.get('d'))
PyJs_anonymous_146_._set_name('anonymous')
@Js
def PyJs_anonymous_147_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['c', 'a', 'b', 'd'])
    var.put('c', Js('{'))
    var.put('d', Js(''))
    for PyJsTemp in var.get('a'):
        var.put('b', PyJsTemp)
        if var.get('a').callprop('hasOwnProperty', var.get('b')):
            if var.get('b').callprop('match', JsRegExp('/^[a-z0-9]+$/i')).neg():
                PyJsTempException = JsToPyException(var.get('sjcl').get('exception').get('invalid').create(Js('json encode: invalid property name')))
                raise PyJsTempException
            var.put('c', (((var.get('d')+Js('"'))+var.get('b'))+Js('":')), '+')
            var.put('d', Js(','))
            while 1:
                SWITCHED = False
                CONDITION = (var.get('a').get(var.get('b')).typeof())
                if SWITCHED or PyJsStrictEq(CONDITION, Js('number')):
                    SWITCHED = True
                    pass
                if SWITCHED or PyJsStrictEq(CONDITION, Js('boolean')):
                    SWITCHED = True
                    var.put('c', var.get('a').get(var.get('b')), '+')
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('string')):
                    SWITCHED = True
                    var.put('c', ((Js('"')+var.get('escape')(var.get('a').get(var.get('b'))))+Js('"')), '+')
                    break
                if SWITCHED or PyJsStrictEq(CONDITION, Js('object')):
                    SWITCHED = True
                    var.put('c', ((Js('"')+var.get('sjcl').get('codec').get('base64').callprop('fromBits', var.get('a').get(var.get('b')), Js(0.0)))+Js('"')), '+')
                    break
                if True:
                    SWITCHED = True
                    PyJsTempException = JsToPyException(var.get('sjcl').get('exception').get('bug').create(Js('json encode: unsupported type')))
                    raise PyJsTempException
                SWITCHED = True
                break
    return (var.get('c')+Js('}'))
PyJs_anonymous_147_._set_name('anonymous')
@Js
def PyJs_anonymous_148_(a, this, arguments, var=var):
    var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
    var.registers(['c', 'a', 'b', 'd'])
    var.put('a', var.get('a').callprop('replace', JsRegExp('/\\s/g'), Js('')))
    if var.get('a').callprop('match', JsRegExp('/^\\{.*\\}$/')).neg():
        PyJsTempException = JsToPyException(var.get('sjcl').get('exception').get('invalid').create(Js("json decode: this isn't json!")))
        raise PyJsTempException
    var.put('a', var.get('a').callprop('replace', JsRegExp('/^\\{|\\}$/g'), Js('')).callprop('split', JsRegExp('/,/')))
    PyJs_Object_149_ = Js({})
    var.put('b', PyJs_Object_149_)
    #for JS loop
    var.put('c', Js(0.0))
    while (var.get('c')<var.get('a').get('length')):
        try:
            if var.put('d', var.get('a').get(var.get('c')).callprop('match', JsRegExp('/^\\s*(?:(["\']?)([a-z][a-z0-9]*)\\1)\\s*:\\s*(?:(-?\\d+)|"([a-z0-9+\\/%*_.@=\\-]*)"|(true|false))$/i'))).neg():
                PyJsTempException = JsToPyException(var.get('sjcl').get('exception').get('invalid').create(Js("json decode: this isn't json!")))
                raise PyJsTempException
            def PyJs_LONG_150_(var=var):
                return (var.get('b').put(var.get('d').get('2'), (var.get('sjcl').get('codec').get('base64').callprop('toBits', var.get('d').get('4')) if var.get('d').get('2').callprop('match', JsRegExp('/^(ct|adata|salt|iv)$/')) else var.get('unescape')(var.get('d').get('4')))) if (var.get(u"null")!=var.get('d').get('4')) else ((var.get(u"null")!=var.get('d').get('5')) and var.get('b').put(var.get('d').get('2'), PyJsStrictEq(Js('true'),var.get('d').get('5')))))
            (var.get('b').put(var.get('d').get('2'), var.get('parseInt')(var.get('d').get('3'), Js(10.0))) if (var.get(u"null")!=var.get('d').get('3')) else PyJs_LONG_150_())
        finally:
                (var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1))
    return var.get('b')
PyJs_anonymous_148_._set_name('anonymous')
@Js
def PyJs_anonymous_151_(a, b, c, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['c', 'a', 'b', 'd'])
    PyJs_Object_152_ = Js({})
    (PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get('a')) and var.put('a', PyJs_Object_152_))
    if PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get('b')):
        return var.get('a')
    for PyJsTemp in var.get('b'):
        var.put('d', PyJsTemp)
        if var.get('b').callprop('hasOwnProperty', var.get('d')):
            if ((var.get('c') and PyJsStrictNeq(PyJsComma(Js(0.0), Js(None)),var.get('a').get(var.get('d')))) and PyJsStrictNeq(var.get('a').get(var.get('d')),var.get('b').get(var.get('d')))):
                PyJsTempException = JsToPyException(var.get('sjcl').get('exception').get('invalid').create(Js('required parameter overridden')))
                raise PyJsTempException
            var.get('a').put(var.get('d'), var.get('b').get(var.get('d')))
    return var.get('a')
PyJs_anonymous_151_._set_name('anonymous')
@Js
def PyJs_anonymous_153_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['c', 'a', 'b', 'd'])
    PyJs_Object_154_ = Js({})
    var.put('c', PyJs_Object_154_)
    for PyJsTemp in var.get('a'):
        var.put('d', PyJsTemp)
        ((var.get('a').callprop('hasOwnProperty', var.get('d')) and PyJsStrictNeq(var.get('a').get(var.get('d')),var.get('b').get(var.get('d')))) and var.get('c').put(var.get('d'), var.get('a').get(var.get('d'))))
    return var.get('c')
PyJs_anonymous_153_._set_name('anonymous')
@Js
def PyJs_anonymous_155_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['c', 'a', 'b', 'd'])
    PyJs_Object_156_ = Js({})
    var.put('c', PyJs_Object_156_)
    #for JS loop
    var.put('d', Js(0.0))
    while (var.get('d')<var.get('b').get('length')):
        try:
            (PyJsStrictNeq(PyJsComma(Js(0.0), Js(None)),var.get('a').get(var.get('b').get(var.get('d')))) and var.get('c').put(var.get('b').get(var.get('d')), var.get('a').get(var.get('b').get(var.get('d')))))
        finally:
                (var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1))
    return var.get('c')
PyJs_anonymous_155_._set_name('anonymous')
PyJs_Object_129_ = Js({'defaults':PyJs_Object_130_,'ja':PyJs_anonymous_131_,'encrypt':PyJs_anonymous_138_,'ia':PyJs_anonymous_139_,'decrypt':PyJs_anonymous_146_,'encode':PyJs_anonymous_147_,'decode':PyJs_anonymous_148_,'g':PyJs_anonymous_151_,'sa':PyJs_anonymous_153_,'ra':PyJs_anonymous_155_})
var.get('sjcl').put('json', PyJs_Object_129_)
var.get('sjcl').put('encrypt', var.get('sjcl').get('json').get('encrypt'))
var.get('sjcl').put('decrypt', var.get('sjcl').get('json').get('decrypt'))
PyJs_Object_157_ = Js({})
var.get('sjcl').get('misc').put('pa', PyJs_Object_157_)
@Js
def PyJs_anonymous_158_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['c', 'a', 'b', 'd'])
    var.put('c', var.get('sjcl').get('misc').get('pa'))
    PyJs_Object_159_ = Js({})
    var.put('b', (var.get('b') or PyJs_Object_159_))
    var.put('d', (var.get('b').get('iter') or Js(1000.0)))
    PyJs_Object_160_ = Js({})
    var.put('c', var.get('c').put(var.get('a'), (var.get('c').get(var.get('a')) or PyJs_Object_160_)))
    PyJs_Object_161_ = Js({'firstSalt':(var.get('b').get('salt').callprop('slice', Js(0.0)) if (var.get('b').get('salt') and var.get('b').get('salt').get('length')) else var.get('sjcl').get('random').callprop('randomWords', Js(2.0), Js(0.0)))})
    var.put('d', var.get('c').put(var.get('d'), (var.get('c').get(var.get('d')) or PyJs_Object_161_)))
    var.put('c', (var.get('d').get('firstSalt') if PyJsStrictEq(PyJsComma(Js(0.0), Js(None)),var.get('b').get('salt')) else var.get('b').get('salt')))
    var.get('d').put(var.get('c'), (var.get('d').get(var.get('c')) or var.get('sjcl').get('misc').callprop('pbkdf2', var.get('a'), var.get('c'), var.get('b').get('iter'))))
    PyJs_Object_162_ = Js({'key':var.get('d').get(var.get('c')).callprop('slice', Js(0.0)),'salt':var.get('c').callprop('slice', Js(0.0))})
    return PyJs_Object_162_
PyJs_anonymous_158_._set_name('anonymous')
var.get('sjcl').get('misc').put('cachedPbkdf2', PyJs_anonymous_158_)
((PyJsStrictNeq(Js('undefined'),var.get('module',throw=False).typeof()) and var.get('module').get('exports')) and var.get('module').put('exports', var.get('sjcl')))
@Js
def PyJs_anonymous_163_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    return var.get('sjcl')
PyJs_anonymous_163_._set_name('anonymous')
(PyJsStrictEq(Js('function'),var.get('define',throw=False).typeof()) and var.get('define')(Js([]), PyJs_anonymous_163_))
pass


# Add lib to the module scope
sjcl = var.to_python()