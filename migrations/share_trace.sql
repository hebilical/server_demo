CREATE TABLE user_share_trace (
    id SERIAL primary key,
    weibo_id INT NOT NULL DEFAULT 0,
    created_by VARCHAR(50) NOT NULL DEFAULT '',
    at_user_list VARCHAR[] NOT NULL DEFAULT '{}',
    created_at TIMESTAMP  WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP  WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
COMMENT ON TABLE user_share_trace IS '用户分享记录';
COMMENT ON COLUMN user_share_trace.weibo_id IS '微博ID';
COMMENT ON COLUMN user_share_trace.at_user_list IS '被分享的用户列表';