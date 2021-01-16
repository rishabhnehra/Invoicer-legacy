import {Story, Meta} from '@storybook/react/types-6-0';

import {BlankCard, BlankCardProps} from './BlankCard';
import { TextInput } from '../../index'

export default {
    title: 'Components/Card',
    component: BlankCard
} as Meta;

const Template: Story<BlankCardProps> = (args) => <BlankCard {...args} />

export const Blank = Template.bind({});
Blank.args = {
    children: <>
        <div>
            <TextInput placeholder="Email" type="email" onClick={() => null} />
        </div>
    </>
}