import sys, os
f = lambda name, kind, ph, tag="input": (
 f'<p><label>{name}<span class="wpcf7-form-control-wrap" data-name="x">'
 + (f'<textarea cols="40" rows="4" class="wpcf7-form-control wpcf7-textarea" placeholder="{ph}"></textarea>' if tag=="textarea"
    else f'<input size="40" class="wpcf7-form-control wpcf7-{kind}" placeholder="{ph}" type="{kind}">')
 + '</span></label></p>')
mock = ('<div class="wpcf7 js"><form class="wpcf7-form init">'
 + f("Name *","text","Your name") + f("Phone number","tel","Your phone number") + f("Email *","email","you@example.com")
 + f("Message *","textarea","Ask us anything about this device","textarea")
 + '<p><input class="wpcf7-form-control wpcf7-submit has-spinner" type="submit" value="Send message"><span class="wpcf7-spinner"></span></p>'
 + '<div class="wpcf7-response-output" aria-hidden="true"></div></form></div>')
src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products", "") + "iphone-15-pro-product-description.html").read()
src=src.replace('[contact-form-7 id="7e17e9a" title="Product enquiry"]', mock)
open("pv_ip.html","w").write(f'<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"><style>body{{margin:0;background:#f6f7f9}}.wrap{{max-width:1120px;margin:0 auto;padding:0 22px;box-sizing:border-box}}.wpcf7-spinner{{visibility:visible;display:inline-block;width:24px;height:24px;border-radius:100%;background:#23282d;opacity:.75}} .wpcf7 form .wpcf7-response-output{{margin:2em .5em 1em;padding:.2em 1em;border:2px solid #00a0d2}} .wpcf7 form.init .wpcf7-response-output{{display:none}}</style></head><body><div class="wrap">{src}</div></body></html>')
