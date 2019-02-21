-- check vid and eid existence

if ngx.var.arg_vid == nil then
    ngx.say("vid: missing")
else
    ngx.say("vid: [", ngx.var.arg_vid, "]")
end

if ngx.var.arg_eid == nil then
    ngx.say("eid: missing")
else
    ngx.say("eid: [", ngx.var.arg_eid, "]")
end

ngx.say("url: [", ngx.var.request_uri, "]")