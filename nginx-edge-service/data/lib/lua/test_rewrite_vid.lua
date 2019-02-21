local redis = require "resty.redis"
local red = redis:new()

ngx.log(ngx.STDERR, "starting test_rewrite_vid")

red:set_timeout(100000) -- 10 sec

local ok, err = red:connect("redis", 6379)

if not ok then
    --ngx.say("failed to connect: ", err)
    return err
end

local res, err = red:get(ngx.var.arg_eid)
if not res then
    --ngx.say("failed to get test: ", err)
    return err
end

if res == ngx.null then
    --ngx.say("this is not redis_data") 
    return nil
end

--ngx.say("final result from redis: ", res)
ngx.log(ngx.STDERR, "final result from redis: ", res)
--ngx.say("final: ", ngx.var.vid)
return ngx.redirect(res);
-- return res .. "tony"