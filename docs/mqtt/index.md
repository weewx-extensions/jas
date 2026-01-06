---
title: MQTT
nav_order: 11
---

## cleanSession =

If `true` the client and server persistent state is deleted on successful connect.

## disconnect =

The number of seconds that the MQTT connection will stay connected (it will be disconnected after this amount).
The default us not set, meaning there is no 'auto disconnect'.

## enable =

Turns MQTT on or off.

## host =

The MQTT server. The default is localhost.

## keepAliveInterval =

Maximum period in seconds allowed between communications with the broker. The default is 60.

## password =

Authentication password for this connection.

## port =

The port to connect to. The default is 1883.

## reconnect =

Sets whether the client will automatically attempt to reconnect to the server if the connection is lost.

## timeout=

If the connect has not succeeded within this number of seconds, it is deemed to have failed.

## topic =

The topic to subscribe to.
Deprecated, use `[[[[[topics]]]]]` and `[[[[[[topic-name]]]]]]`.

## username =

Authentication username for this connection.

## useSSL =

If true, use an SSL Websocket connection.

## `[[[[[topics]]]]]`

Each subsection is a topic to subscribe to.

### `[[[[[[topic-name]]]]]]`

Each topic to subscribe to has its own section that is the name of the topic to subscribe to.

#### `[[[[[[[fields]]]]]]]`

Each subsection us a field that needs to be configured.

##### `[[[[[[[[field-name]]]]]]]]`

The name of the observation in the MQTT payload.

###### name =

The WeeWX name.
