var React = require('react');
var ReactDOM = require('react-dom');
var Tether = require('react-tether');
var antd =  require('antd');


ReactDOM.render(
  <antd.Timeline>
    <antd.Timeline.Item>Create a services site 2015-09-01</antd.Timeline.Item>
    <antd.Timeline.Item>Solve initial network problems 2015-09-01</antd.Timeline.Item>
    <antd.Timeline.Item dot={<Icon type="clock-circle-o" style={{ fontSize: '16px' }} />} color="red">Technical testing 2015-09-01</antd.Timeline.Item>
    <antd.Timeline.Item>Network problems being solved 2015-09-01</antd.Timeline.Item>
  </antd.Timeline>
, mountNode);
