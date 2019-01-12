__all__ = ['bigint']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['BigInt'])
var.put('BigInt', var.get('BigInteger'))
var.get('BigInt').put('TWO', var.get('BigInt').create(Js('2'), Js(10.0)))
@Js
def PyJs_anonymous_0_(callback, fail_callback, this, arguments, var=var):
    var = Scope({'callback':callback, 'fail_callback':fail_callback, 'this':this, 'arguments':arguments}, var)
    var.registers(['fail_callback', 'callback'])
    var.get('callback')()
PyJs_anonymous_0_._set_name('anonymous')
var.get('BigInt').put('setup', PyJs_anonymous_0_)
@Js
def PyJs_anonymous_1_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    return var.get(u"this").callprop('toString')
PyJs_anonymous_1_._set_name('anonymous')
var.get('BigInt').get('prototype').put('toJSONObject', PyJs_anonymous_1_)
@Js
def PyJs_anonymous_2_(s, this, arguments, var=var):
    var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
    var.registers(['s'])
    return var.get('BigInt').create(var.get('s'), Js(10.0))
PyJs_anonymous_2_._set_name('anonymous')
var.get('BigInt').put('fromJSONObject', PyJs_anonymous_2_)
@Js
def PyJs_anonymous_3_(i, this, arguments, var=var):
    var = Scope({'i':i, 'this':this, 'arguments':arguments}, var)
    var.registers(['i'])
    return var.get('BigInt').callprop('fromJSONObject', (Js('')+var.get('i')))
PyJs_anonymous_3_._set_name('anonymous')
var.get('BigInt').put('fromInt', PyJs_anonymous_3_)
var.get('BigInt').put('use_applet', Js(False))
pass


# Add lib to the module scope
bigint = var.to_python()