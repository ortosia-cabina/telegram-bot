__all__ = ['elgamal']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([])
PyJs_Object_0_ = Js({})
var.put('ElGamal', PyJs_Object_0_)
var.get('ElGamal').put('BITS', Js(256.0))
@Js
def PyJs_anonymous_1_(max, this, arguments, var=var):
    var = Scope({'max':max, 'this':this, 'arguments':arguments}, var)
    var.registers(['random', 'rand_bi', 'max'])
    pass
    var.put('random', var.get('sjcl').get('random').callprop('randomWords', Js(100.0), Js(0.0)))
    var.put('rand_bi', var.get('BigInt').create(var.get('sjcl').get('codec').get('hex').callprop('fromBits', var.get('random')), Js(16.0)))
    return var.get('rand_bi').callprop('mod', var.get('max'))
    return var.get('BigInt').callprop('_from_java_object', var.get('random')).callprop('mod', var.get('max'))
PyJs_anonymous_1_._set_name('anonymous')
var.get('ElGamal').put('getRandomInteger', PyJs_anonymous_1_)
@Js
def PyJs_anonymous_2_(pk, m, r, this, arguments, var=var):
    var = Scope({'pk':pk, 'm':m, 'r':r, 'this':this, 'arguments':arguments}, var)
    var.registers(['beta', 'q', 'q1', 'pk', 'r', 'alpha', 'm'])
    if var.get('m').callprop('equals', var.get('BigInt').get('ZERO')):
        PyJsTempException = JsToPyException(Js("Can't encrypt 0 with El Gamal"))
        raise PyJsTempException
    if var.get('r').neg():
        var.put('q', var.get('BigInt').callprop('fromInt', Js(2.0)).callprop('pow', var.get('ElGamal').get('BITS')))
        var.put('q1', var.get('q').callprop('subtract', var.get('BigInt').get('ONE')))
        var.put('r', var.get('ElGamal').callprop('getRandomInteger', var.get('q1')))
    var.put('alpha', var.get('pk').get('g').callprop('modPow', var.get('r'), var.get('pk').get('p')))
    var.put('beta', var.get('pk').get('y').callprop('modPow', var.get('r'), var.get('pk').get('p')).callprop('multiply', var.get('m')).callprop('mod', var.get('pk').get('p')))
    PyJs_Object_3_ = Js({'alpha':var.get('alpha'),'beta':var.get('beta')})
    return PyJs_Object_3_
PyJs_anonymous_2_._set_name('anonymous')
var.get('ElGamal').put('encrypt', PyJs_anonymous_2_)
pass


# Add lib to the module scope
elgamal = var.to_python()