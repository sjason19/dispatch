import React from 'react'

import EventSelectInput from '../inputs/selects/EventSelectInput'

export default function EventField(props) {
  return (
    <EventSelectInput
      value={props.data}
      many={props.field.many}
      onChange={selected => props.onChange(selected)} />
  )
}
