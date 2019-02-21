function set_vid(eid)
    -- connect to redis to get vid based on eid
    local redis = require "resty.redis"
    local red = redis:new()
    
    red:set_timeout(100000) -- 10 sec
    
    local ok, err = red:connect("redis", 6379)
    
    if not ok then
        ngx.print("failed to connect: ", err)
        ngx.log(ngx.NOTICE, "failed to connect: " .. err)
        return err
    end

    local res, err = red:get(eid)
    if not res then
        ngx.log(ngx.NOTICE, "failed to get eid2vid from redis: " .. err)
        return err
    end

    if res == ngx.null then
        ngx.log(ngx.NOTICE, "this is not redis_data")
        return nil
    end

    return res
end

-- instruction: steps in this lua
-- 1. rewrite uri
-- 2. eid2vid in redis
-- 3. set new args

local uri = ngx.re.sub(ngx.var.uri, "^/relua/(.*)", "/api", "o")
ngx.log(ngx.NOTICE, uri)
local args = ngx.req.get_uri_args()
local new_args = nil
for key, val in pairs(args) do
    if type(val) == "table" then
        -- ngx.say(key, ": ", table.concat(val, ", "))
        -- new_args = new_args .. "&" .. key .. "=" .. table.concat(val, ",")
    else
        -- ngx.say(key, ": ", val)
        if key == "eid" then
            local vid = set_vid(val)
            if new_args ~= nil then
                new_args = new_args .. "&" .. "vid" .. "=" .. vid
            else
                new_args = "vid" .. "=" .. vid
            end

        else
            if new_args ~= nil then
                new_args = new_args .. "&" .. key .. "=" .. val
            else
                new_args = key .. "=" .. val
            end
        end
    end
end
-- ngx.print(new_args)
ngx.log(ngx.STDERR, ngx.var.scheme .. "://".. ngx.var.apihost  .. uri .. "?" .. new_args)
ngx.log(ngx.STDERR, ngx.var.apihost)
ngx.log(ngx.STDERR, uri)
ngx.log(ngx.STDERR, new_args)
ngx.log(ngx.STDERR, "here is a test")
ngx.req.set_uri_args(new_args)
ngx.req.set_uri(uri, true)


