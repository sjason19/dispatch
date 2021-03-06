import React from 'react'

import PollSelectInput from '../inputs/selects/PollSelectInput'

export default function PollField(props) {
  return (
    <PollSelectInput
      value={props.data}
      many={props.field.many}
      onChange={selected => props.onChange(selected)} />
  )
}
